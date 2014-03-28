# -*- coding: utf-8 -*-

from django.forms import ModelForm, CharField
from django.contrib.admin import ModelAdmin, site

from ckeditor.widgets import CKEditorWidget

from article.settings import USE_PORTLET
from article.models import Article


class CKEditorForm(ModelForm):
    text = CharField(widget=CKEditorWidget())

    class Meta:
        model = Article


class ArticleAdmin(ModelAdmin):
    form = CKEditorForm
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ['author']
    list_display = ('title', 'author', 'created', 'modified')


site.register(Article, ArticleAdmin)


if USE_PORTLET:
    from article.models import ArticlePortlet
    from portlet.admin import PortletAdmin
    site.register(ArticlePortlet, PortletAdmin)
