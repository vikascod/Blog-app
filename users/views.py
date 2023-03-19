from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from users.forms import SignupForm, ProfileEditForm, ManualChangePasswordForm, CreateUserProfileForm, UpdateUserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from app.models import Profile
from django.views import View


class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateUserProfileForm
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileview(UpdateView):
    model = Profile
    form_class = UpdateUserProfileForm
    template_name = 'registration/edit_user_profile.html'
    # fields = ['bio', 'profile_pic', 'facebook_url', 'insta_url', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('index')

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)

        profile_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile_user'] = profile_user
        return context

def change_password(request):
    return render(request, 'registration/password_success.html')


class RegistationView(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileEditView(UpdateView):
    form_class = ProfileEditForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('index')

    #this func helps to return data
    def get_object(self):
        return self.request.user


class ChangePassword1View(PasswordChangeView):
    form_class = ManualChangePasswordForm
    success_url = reverse_lazy('password_changed')


def aboutView(request):
    return render(request, 'registration/about.html')