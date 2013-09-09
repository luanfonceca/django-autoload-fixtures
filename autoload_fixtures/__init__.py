#!/usr/bin/env python
# encoding: utf-8

"""
autoload_fixtures/__init__.py

Created by Luan Fonseca <luanfonceca@gmail.com> on 2013-08-08
"""

from django.dispatch import receiver
from django.db.models.loading import get_models, get_app
from south.signals import post_migrate

@receiver(post_migrate)
def loadd_fixtures_for_app(sender, **kwargs):
    app_name = kwargs.get('app')
    if not app_name: return

    print u"Running autoload fixtures for %s:" % app_name
    for model in get_models(get_app(app_name)):
        print u" > %s:%s" % (app_name, model.__name__.lower())