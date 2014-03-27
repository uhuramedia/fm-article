"""Settings for fm.article"""
from django.conf import settings


USE_PORTLET = getattr(settings, 'ARTICLE_USE_PORTLET', True)

PAGINATION = getattr(settings, 'ARTICLE_PAGINATION', True)

ITEMS_PER_PAGE = getattr(settings, 'ARTICLE_ITEMS_PER_PAGE', 5)
