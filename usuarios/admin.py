from django.contrib import admin

# Register your models here.
from .models import Avatar

register_models = [Avatar]

admin.site.register(register_models)
