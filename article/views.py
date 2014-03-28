# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from article.settings import PAGINATION, ITEMS_PER_PAGE
from article.models import Article


def teaser(request):
    article = Article.objects.order_by('-release_date')[:3]

    return render_to_response(
        'article/teaser.html',
        locals(),
        RequestContext(request)
    )


def articles(request):
    articles = Article.objects.order_by('-release_date')

    if PAGINATION:
        paginator = Paginator(articles, ITEMS_PER_PAGE)
        p = request.GET.get('page', 1)

        try:
            article = paginator.page(p)
        except PageNotAnInteger:
            article = paginator.page(1)
        except EmptyPage:
            article = paginator.page(paginator.num_pages)

        article_range = _get_smaller_range(
            article.number,
            article.paginator.num_pages,
            article.paginator.page_range
        )

    return render_to_response(
        'article/articles.html',
        locals(),
        RequestContext(request)
    )


def article(request, slug):
    if request.GET.get('type', False) == 'modal':
        extend = '-inner'
    else:
        extend = ''

    article = get_object_or_404(Article, slug=slug)

    return render_to_response(
        'article/single%s.html' % extend,
        locals(),
        RequestContext(request)
    )


def _get_smaller_range(current, max, range):
    prev = None
    next = None

    if current >= 3:
        prev = current - 3

    if current <= max - 3:
        next = current + 2

    return range[prev:next]
