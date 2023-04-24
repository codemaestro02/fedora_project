from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BlogPostCreateForm, CommentCreateForm
from .models import BlogPost, Category, Comment


def index(request):
    blogs = BlogPost.objects.all()[:12:-1]
    context = {
        "blogs": blogs,
    }
    return render(request, 'blog/blog.html', context=context)
# Create your views here.


@login_required(login_url='login')
def like_view(request, slug):
    if request.method == 'POST':
        blog = get_object_or_404(BlogPost, id=slug)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)
        return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))
    
    
def blog_search(request):
    if request.user.is_authenticated:
        all_blogs = BlogPost.active_blogs.all()
        search_by_word = request.GET.get('w') if request.GET.get('w') is not None else all_blogs
        search_by_year = request.GET.get('y') if request.GET.get('d') is not None else all_blogs
        search_by_month = request.GET.get('m') if request.GET.get('d') is not None else all_blogs
        search_by_day = request.GET.get('d') if request.GET.get('d') is not None else all_blogs
        blogs = BlogPost.objects.filter(
            Q(title__icontains=search_by_word) |
            Q(author__icontains=search_by_word) |
            Q(description__icontains=search_by_word) |
            Q(keywords__icontains=search_by_word) |
            Q(tags__icontains=search_by_word) |
            Q(category__icontains=search_by_word) |
            Q(created__year=search_by_year) |
            Q(created__month=search_by_month) |
            Q(created__day=search_by_day)
        )
    blog_count = blogs.count()
    context = {
        'blogpost_list': blogs,
        'blog_count': blog_count,
    }
    return render(request, 'blog/blog_list.html', context)


def search(request):
    keywords = ''

    if request.method == 'POST': # form was submitted

        keywords = request.POST.get("keywords", "")  # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('title', 'keywords', 'description')  # change accordingly
        for keyword in keywords.split(' '):  # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        blogs = BlogPost.objects.filter(all_queries).distinct()
        context = {'blogpost_list': blogs}
        return render(request, 'blog/blog_list.html', context)
    else:  # no data submitted
        context = {}
        return render(request, 'blog/blog_list.html', context)


class BlogPostCreateView(LoginRequiredMixin ,CreateView):
    model = BlogPost
    form_class = BlogPostCreateForm
    template_name = "blog/blog_create.html"


def blog_create(request):
    form = BlogPostCreateForm()
    if request.method == 'POST':
        form = BlogPostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog-list')
        context = {
            'form': form,
        }
        return render(request, 'blog/blog_create.html', context)
        


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/blog_create.html"


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
       
       
class BlogPostDetailView(DetailView):
    
    model = BlogPost
    template_name = 'blog/blog-single.html'
    slug_url_kwargs = 'slug'
    # query_pk_and_slug = True
    

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    
    tags = blog.tags.all()
    
    if request.user.is_authenticated and blog.author == request.user:
        comments = blog.comment_set.all()
    else:
        comments = blog.comment_set.active_comments.all()
    

    form = CommentCreateForm()
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.blogpost = blog
            comment_form.author = request.user
            comment_form.save()
            return redirect('blog_detail', blog.slug)

    if blog.likes.filter(id=request.user.id).exists():
        like = True
    else:
        like = False
    context = {
        'blog': blog,
        'blog_likes': blog.total_likes,
        'form': form,
        'comments': comments,
        'like': like,
        'tags': tags,
    }
    return render(request, 'blog/blog-single.html', context)


@login_required(login_url='login')
def hide_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    blog = BlogPost.objects.get(comment=comment)
    comment.is_hidden = not comment.is_hidden
    comment.save()
    return redirect(reverse_lazy('blog_detail', kwargs={'slug': blog.slug}))
