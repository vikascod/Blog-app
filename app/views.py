from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import Post, Category, Comment
from app.forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.db.models import Q


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class IndexView(ListView):
    model = Post
    # context_object_name
    template_name = 'app/index.html'
    ordering = ['-created_on']


def categoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'app/category.html', {'cats':cats.title(), 'category_post':category_post})


class IndexDetailView(DetailView):
    model = Post
    # context_object_name
    template_name = 'app/details.html'

    def get_context_data(self, *args, **kwargs):
        cat_manu = Category.objects.all()
        context = super(IndexDetailView, self).get_context_data()

        obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_like = obj.total_likes()

        liked = False
        if obj.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_like'] = total_like
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/add_posts.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'app/add_comment.html'
    ordering = ['-id']
    def get_success_url(self):
        detail_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={'pk':detail_id})

    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)



class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'app/update.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'app/delete_post.html'
    success_url = reverse_lazy('index')


def search(request):
    search_query = request.GET.get('query')
    blogs = Post.objects.filter(
        Q(title__contains=search_query)|
        Q(body__contains=search_query)
    )
    context = {'blogs':blogs}
    return render(request, 'app/search_blogs.html', context)