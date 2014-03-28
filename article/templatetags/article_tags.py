# -*- coding: utf-8 -*-

from django import template
from django.shortcuts import get_list_or_404

from article.models import Article

register = template.Library()


@register.inclusion_tag('article/tease_article.html')
def tease_article():
    return {
        'articles': Article.objects.all()[:2]
    }
