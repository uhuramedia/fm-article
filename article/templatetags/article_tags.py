# -*- coding: utf-8 -*-

from django import template

from article.models import Article

register = template.Library()


@register.inclusion_tag('article/tease_article.html')
def tease_article():
    return {
        'articles': Article.objects.all()[:2]
    }


@register.inclusion_tag('article/feature_article.html')
def feature_article():
    return {
        'articles': Article.objects.values('slug', 'title')[0:3]
    }
