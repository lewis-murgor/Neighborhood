from django.contrib import admin
from .models import Neighborhood,Business,Profile

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Profile)
