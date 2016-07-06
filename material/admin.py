from django.contrib import admin

# Register your models here.
from .models import *

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc')
    search_fields = ['code','name','desc']
    #list_filter = ['factory__name']
    #inlines = [ChoiceInlineForMaterial]

class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc')
    search_fields = ['code','name','desc']
    #list_filter = ['factory__name']
    #inlines = [ChoiceInlineForMaterial]

admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialCategory, MaterialCategoryAdmin)
    