# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from models import Article

def teaser(request):
    context = {}
    context['article'] = Article.objects.order_by('-release_date')[:3]

    return render_to_response(
            'article/teaser.html',
            context,
            RequestContext(request))

def archive(request):
    context = {}
    article_set = Article.objects.order_by('-release_date')[3:]
    paginator = Paginator(article_set, 5)
    page = request.GET.get('page', 1)

    try:
        context['article'] = paginator.page(page)
    except PageNotAnInteger:
        context['article'] = paginator.page(1)
    except EmptyPage:
        context['article'] = paginator.page(paginator.num_pages)

    context['range'] = _get_smaller_range(
        context['article'].number,
        context['article'].paginator.num_pages,
        context['article'].paginator.page_range
    )

    return render_to_response(
            'article/archive.html',
            context,
            RequestContext(request))

def single(request, slug):
    context = {}

    context['article'] = Article.objects.get(slug=slug)

    return render_to_response(
            'article/single.html',
            context,
            RequestContext(request))

def _get_smaller_range(current, max, range):
    prev = None
    next = None

    if current >= 3:
        prev = current - 3

    if current <= max-3:
        next = current + 2

    return range[prev:next]
