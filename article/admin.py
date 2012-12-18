# -*- coding: utf-8 -*-

from django.forms import ModelForm, CharField
from django.contrib.admin import ModelAdmin, site
from tinymce.widgets import TinyMCE
from portlet.admin import PortletAdmin
from models import Article, ArticlePortlet

class ArticleTinyMCEForm(ModelForm):
        text = CharField(
            widget=TinyMCE(attrs={'cols': 150, 'rows': 80}))

        class Meta:
            model = Article

class ArticleAdmin(ModelAdmin):
    form = ArticleTinyMCEForm
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ['author']

site.register(Article, ArticleAdmin)
site.register(NewsPortlet, PortletAdmin)
