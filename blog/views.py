from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return render(request, 'blog/news.html')
    category = request.GET.get('category')  # получаем ?category=news

    if category:
        posts = Post.objects.filter(category=category).order_by('-created_at')
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
    else:
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

    return render(request, 'blog/news.html', {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_category': category
    })
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })