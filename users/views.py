from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from users.forms import SignupForm, ProfileEditForm, ManualChangePasswordForm, CreateUserProfileForm, UpdateUserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from app.models import Profile
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse


from django_ratelimit.decorators import ratelimit



class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = CreateUserProfileForm
    template_name = 'registration/create_user_profile.html'

    ratelimit_key = 'user'
    ratelimit_rate = '5/m'
    ratelimit_block = True
    ratelimit_method = ['POST']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class EditProfileview(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UpdateUserProfileForm
    template_name = 'registration/edit_user_profile.html'
    # fields = ['bio', 'profile_pic', 'facebook_url', 'insta_url', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('index')



class ShowProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         # If the user is not authenticated, redirect to login page
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        profile_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile_user'] = profile_user
        return context


@login_required(login_url='login')
@ratelimit(key='post:username', rate='2/m')
@ratelimit(key='post:tenant', rate='2/m')
def change_password(request):
    return render(request, 'registration/password_success.html')


class RegistationView(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('index')

    #this func helps to return data
    @ratelimit(key='post:q', rate='2/m')
    def get_object(self):
        return self.request.user



class ChangePassword1View(LoginRequiredMixin, PasswordChangeView):
    form_class = ManualChangePasswordForm
    success_url = reverse_lazy('password_changed')


def aboutView(request):
    return render(request, 'registration/about.html')


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Already logged in!")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        
        
    return render(request, 'registration/login.html')

        

