=====
Users
=====

Users is a Django app form user authentication implemantation.
The application provides us with a ready user authentication interface with templates ready for style change.
App was created for my own needs.

Detailed documentation is in the "docs" directory.

Install app
-----------
python -m pip install --user django-users/dist/django-users-0.1.tar.gz

Uninstall app
-------------
python -m pip uninstall django-users


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'users',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),


3. Run ``python manage.py migrate`` to create the polls models.

4. Visit http://127.0.0.1:8000/users/ to see available urls.


