from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInlineForRegion(admin.TabularInline):
    model = Factory
    extra = 0

class RegionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'short_name', 'parent', 'desc')
    search_fields = ['name','code','short_name']
    #list_filter = ['nation__name']
    inlines = [ChoiceInlineForRegion]

class ChoiceInlineForCompany(admin.TabularInline):
    model = Department
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    inlines = [ChoiceInlineForCompany]

class ChoiceInlineForDepartment(admin.TabularInline):
    model = Line
    extra = 0

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'company')
    search_fields = ['company__name']
    list_filter = ['company__name']
    inlines = [ChoiceInlineForDepartment]

class ChoiceInlineForFactory(admin.TabularInline):
    model = Workshop
    extra = 0

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'company', 'region')
    search_fields = ['region__name']
    list_filter = ['region__name']
    inlines = [ChoiceInlineForFactory]

class ChoiceInlineForWorkshop(admin.TabularInline):
    model = Line
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'factory')
    #search_fields = ['factory']
    search_fields = ['factory__name']
    list_filter = ['factory__name']
    inlines = [ChoiceInlineForWorkshop]

class ChoiceInlineForLine(admin.TabularInline):
    model = Station
    extra = 0

class LineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'line_type', 'workshop', 'department')
    list_filter = ['workshop__name','department__name','line_type']
    inlines = [ChoiceInlineForLine]

class StationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'line')
    list_filter = (('line__name'),)
    #inlines = [ChoiceInlineForStation]

admin.site.register(Region, RegionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
