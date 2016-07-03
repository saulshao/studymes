from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInlineForNation(admin.TabularInline ):
    model = City
    extra = 0

class NationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    inlines = [ChoiceInlineForNation]

class ChoiceInlineForCity(admin.TabularInline ):
    model = Factory
    extra = 0

class CityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'nation')
    search_fields = ['nation__name']
    list_filter = ['nation__name']
    inlines = [ChoiceInlineForCity]

class ChoiceInlineForCompany(admin.TabularInline ):
    model = Department
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    inlines = [ChoiceInlineForCompany]

class ChoiceInlineForDepartment(admin.TabularInline ):
    model = Line
    extra = 0

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'company')
    search_fields = ['company__name']
    list_filter = ['company__name']
    inlines = [ChoiceInlineForDepartment]

class ChoiceInlineForFactory(admin.TabularInline ):
    model = Workshop
    extra = 0

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'company', 'city')
    search_fields = ['city__name']
    list_filter = ['city__name']
    inlines = [ChoiceInlineForFactory]

class ChoiceInlineForWorkshop(admin.TabularInline ):
    model = Line
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'factory')
    #search_fields = ['factory']
    search_fields = ['factory__name']
    list_filter = ['factory__name']
    inlines = [ChoiceInlineForWorkshop]

class ChoiceInlineForLine(admin.TabularInline ):
    model = Station
    extra = 0

class LineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'line_type', 'workshop', 'department')
    list_filter = ['workshop__name','department__name','line_type']
    inlines = [ChoiceInlineForLine]

class StationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'line')
    search_fields = ['line__name']
    #inlines = [ChoiceInlineForStation]

admin.site.register(Nation, NationAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
