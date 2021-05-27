from django.apps import apps
from django.contrib import admin

models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        print(f'The {model} was registered already!')
