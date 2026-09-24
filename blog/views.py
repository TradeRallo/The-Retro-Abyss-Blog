from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
import calendar
from datetime import datetime
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

def normalize_date(year, month):
    while month > 12:
        month -= 12
        year += 1
    while month < 1:
        month += 12
        year -= 1
    return year, month

def news(request):
    # Текущее время сайта
    now = getattr(settings, 'SITE_TIME', datetime.now())

    # Категория
    category = request.GET.get('category')

    # Выбранные месяц и год
    selected_month = request.GET.get('month')
    selected_year = request.GET.get('year')

    # Включена ли фильтрация по дате
    filter_by_date = request.GET.get('filter_date') == 'on'

    # Если дата не выбрана — используем текущую дату сайта
    year = int(selected_year) if selected_year else now.year
    month = int(selected_month) if selected_month else now.month

    # Список доступных годов
    years = list(range(2007, 2101))

    months = list(enumerate(calendar.month_name))[1:]

    # Получаем все посты
    posts = Post.objects.all()

    # Фильтрация по категории
    if category:
        posts = posts.filter(category=category)

    # Фильтрация по месяцу и году
    if filter_by_date:
        posts = posts.filter(
            created_at__year=year,
            created_at__month=month
        )

    # Сначала новые посты
    posts = posts.order_by('-created_at')

    # Пагинация
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/news.html', {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_category': category,
        'year': year,
        'years': years,
        'month': month,
        'months': months,
        'now': now,
        'filter_by_date': filter_by_date,
    })

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })