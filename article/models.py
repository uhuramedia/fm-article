# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model, ForeignKey, CharField, DateTimeField, \
    SlugField, ImageField, FileField, TextField, IntegerField

from portlet.models import Portlet

class DateAwareModel(Model):
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Article(DateAwareModel):
    author = ForeignKey(User)
    language = CharField('Sprache', max_length=5, db_index=True,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGES[0])
    title = CharField(_('Title'), max_length=150)
    teaser = TextField(_('Teaser'))
    text = TextField(_('Text'))
    image = ImageField(_('Image'), upload_to='articleimages/', blank=True)
    file = FileField(_('PDF'), upload_to='articlepdf/', blank=True)

    slug = SlugField(_('Slug'), unique=True)
    release_date = DateTimeField(_('Date'))

    def __unicode__(self):
        return self.title

class ArticlePortlet(Portlet):
    template = 'article/portlet.html'
    news_amount = IntegerField(_('Displaying amount of articles'))

    def news(self):
        return Article.objects.order_by('-release_date')[:self.news_amount]
