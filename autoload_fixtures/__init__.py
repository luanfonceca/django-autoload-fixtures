#!/usr/bin/env python
# encoding: utf-8

"""
autoload_fixtures/__init__.py

Created by Luan Fonseca <luanfonceca@gmail.com> on 2013-09-08
"""

from django.dispatch import receiver
from django.core.management import call_command
from django.db.models.loading import get_models, get_app
from south.signals import post_migrate

@receiver(post_migrate)
def load_fixtures_for_app(sender, **kwargs):
    app_name = kwargs.get("app")
    if not app_name: return

    print u"Running autoload fixtures for %s:" % app_name
    for model in get_models(get_app(app_name)):
        model_name = model.__name__.lower()
        print u" > %s:%s" % (app_name, model_name)
        fixture_path = "%(app_name)s/fixtures/%(model_name)s.json" % {
            "app_name": app_name,
            "model_name": model_name
        }
        call_command("loaddata", fixture_path)
