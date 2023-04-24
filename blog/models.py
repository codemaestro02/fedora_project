from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from author.decorators import with_author

# Create your models here.


class ActiveManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActiveManager, self).get_queryset()
        return queryset.filter(is_hidden=False)


class HiddenManager(models.Manager):
    def get_queryset(self):
        queryset = super(HiddenManager, self).get_queryset()
        return queryset.filter(is_hidden=True)


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Category(models.Model):  # Category for the Article
    title = models.CharField(max_length=200)  # Title of the Category
    created_on = models.DateTimeField(auto_now_add=True)  # Date of creation

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


@with_author
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the Article
    # slug = models.SlugField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')
    # Unique identifier for the article
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Author of the Article
    description = models.CharField(max_length=500)  # Short Description of the article
    content = RichTextUploadingField(config_name='awesome_ckeditor')  # Content of the article,
    # you need to install CKEditor
    # content = models.TextField()
    # tags = models.ForeignKey('Tag', on_delete = models.SET_NULL, null=True) 
    tags = TaggableManager(_("Tags"), help_text=_("A comma-separated list of tags"))
    # Tags for a Particular Article, You need to install Taggit
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)  # Category of the article
    keywords = models.CharField(max_length=250)  # Keywords to be used in SEO
    cover = models.ImageField(upload_to='images/')  # Cover Image of the article
    quote = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # Date of creation
    updated = models.DateTimeField(auto_now=True)  # Date of update
    status = models.IntegerField(choices=STATUS, default=0)  # Status of the Article either Draft or Published
    likes = models.ManyToManyField(User, related_name="like", blank=True)
    is_hidden = models.BooleanField(default=False)
    
    objects = models.Manager()
    active_blogs = ActiveManager()
    hidden_blogs = HiddenManager()
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-title']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.slug)])


@with_author
class Comment(models.Model):
    blogpost = models.ForeignKey("BlogPost", on_delete=models.CASCADE, null=True)
    comment_message = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_hidden = models.BooleanField(default=False)

    objects = models.Manager()
    active_comments = ActiveManager()
    hidden_comments = HiddenManager()
    
    def __str__(self):
        return f"{self.author} -- {self.updated}"
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
