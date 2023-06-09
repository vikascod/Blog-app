from django import forms
from app.models import Post, Category, Comment

categories = [('Artical', 'Artical'), ('Sports', 'Sports'), ('Entertenment', 'Entertenment'), ('Technology', 'Technology'), ('Business', 'Business'), ('Travel', 'Travel'), ('Education', 'Education'), ('Food and Drinks', 'Food and Drinks'), ('Biography', 'Biography')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'author', 'category', 'body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'name', 'type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=categories, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }