iHela Provider
==============

iHela Provider is a simple Django app to enable oAuth2 authentication with django-allauth.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Install [django-allauth](https://github.com/pennersr/django-allauth)
    `pip install django-allauth` and following the [install guide](https://django-allauth.readthedocs.io/en/latest/installation.html)
1. Add "ihelaprovider" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "vendor_apps.ihelaprovider",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("oAuth2/", include("ihelaprovider.urls")),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to the iHela provider with the application credentials given (you'll need the Admin app enabled).

Visit [iHela](https://ihela.online) and [django-allauth](https://github.com/pennersr/django-allauth).
