# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


VERSION = '0.1'

setup(
    name='fm.article',
    version=VERSION,
    author=u'Daniel Brüggemann',
    author_email='daniel@freshmilk.tv',
    url='http://www.freshmilk.tv',
    description="""Freshmilk article app""",
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    license='WTFPL2',
    install_requires=['django-ckeditor', 'fm.utils', 'fm.portlet']
)
