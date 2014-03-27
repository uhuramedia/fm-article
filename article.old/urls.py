from django.conf.urls.defaults import patterns

urlpatterns = patterns('article.views.',
    (r'^archive/$', 'archive'),
    (r'^(?P<slug>.*)/$', 'single'),
)
