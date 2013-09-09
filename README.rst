****************************************
Django Autoload Fixtures
****************************************
This library allows you to load initial Fixtures automagically after the `South` migrate your `Model`

============
Installation
============

The latest **stable version** of autoload-fixtures can always be installed or updated
to via ``pip`` (prefered) or ``easy_install``:

.. code-block:: bash

    $ pip install --upgrade django-autoload-fixtures

Alternatively:

.. code-block:: bash

    $ easy_install --upgrade django-autoload-fixtures

=====
Usage
=====

Set the new app inside your ``INSTALLED_APPS`` from ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'autoload_fixtures',
        ...
    )

    
Create the ``model_name.json`` files inside your ``project/app_name/fixtures/`` dir, if you already have data inside your models and want to use:

.. code-block:: bash

    $ python manage.py dumpdata app_name.model_name --natural --indent=4 >> app_name/fixtures/model_name.json


Migrate your project, using the ``south`` command:

.. code-block:: bash

    $ python manage.py migrate
