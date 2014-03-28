# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.urlresolvers import reverse

from article.settings import USE_PORTLET

from fm.utils.models import DateAwareModel


class Article(DateAwareModel):
    author = models.ForeignKey(User)
    language = models.CharField(
        _('Language'),
        max_length=5,
        db_index=True,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGES[0]
    )
    title = models.CharField(_('Title'), max_length=150)
    teaser = models.TextField(_('Teaser'), blank=True)
    text = models.TextField(_('Text'))
    image = models.ImageField(_('Image'), upload_to='articleimages/',
                              blank=True)
    file = models.FileField(_('PDF'), upload_to='articlepdf/', blank=True)

    slug = models.SlugField(_('Slug'), unique=True)
    release_date = models.DateTimeField(_('Date'))

    class Meta:
        ordering = ('release_date',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])


if USE_PORTLET:
    from portlet.models import Portlet


    class ArticlePortlet(Portlet):
        template = 'article/portlet.html'
        article_amount = models.IntegerField(
            _('Displaying amount of articles'),
            default=3
        )

        class Meta:
            ordering = ('modified',)

        def article(self):
            return Article.objects\
                .order_by('-release_date')[:self.article_amount]
