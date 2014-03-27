from django.conf.urls import patterns, url

urlpatterns = patterns('article.views',
    url(r'^$', 'articles', name='articles'),
    url(r'^(?P<slug>.*)/$', 'article', name='article'),
)
