from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Nation)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Factory)
admin.site.register(Workshop)
admin.site.register(Line)