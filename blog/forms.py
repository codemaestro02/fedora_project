from django.forms import ModelForm

from .models import BlogPost, Category, Comment, Tag


class BlogPostCreateForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['author']


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['blogpost', 'author', 'is_hidden']
    