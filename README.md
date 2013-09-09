Autoload-Fixtures
====================

This library allows you to load initial Fixtures automagically after the `South` migrate your `Model`


##How To use
1.  Instal this app from Pypi

  `$ pip install django-autoload-fixtures`
2.   Set the new app inside your `INSTALLED_APPS`.

  ```python
  INSTALLED_APPS = (
        ...
        'autoload_fixtures',
        ...
  )
  ```
3.  Create the `MODELNAME.json` files inside your `project/app/fixtures/` dir.
4.  Migrate your project

  `python manage.py migrate`
