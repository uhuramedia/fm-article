# -*- coding: utf-8 -*-

from django.forms import ModelForm, CharField
from django.contrib.admin import ModelAdmin, site
from ckeditor.widgets import CKEditorWidget
from portlet.admin import PortletAdmin
from models import Article, ArticlePortlet


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
site.register(ArticlePortlet, PortletAdmin)
