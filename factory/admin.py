from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInlineForNation(admin.TabularInline ):
    model = City
    extra = 0

class NationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc')
    inlines = [ChoiceInlineForNation]

class ChoiceInlineForCity(admin.TabularInline ):
    model = Factory
    extra = 0

class CityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc', 'nation')
    inlines = [ChoiceInlineForCity]

class ChoiceInlineForCompany(admin.TabularInline ):
    model = Department
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc')
    inlines = [ChoiceInlineForCompany]

class ChoiceInlineForDepartment(admin.TabularInline ):
    model = Line
    extra = 0

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc', 'company')
    inlines = [ChoiceInlineForDepartment]

class ChoiceInlineForFactory(admin.TabularInline ):
    model = Workshop
    extra = 0

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc', 'company', 'city')
    inlines = [ChoiceInlineForFactory]

class ChoiceInlineForWorkshop(admin.TabularInline ):
    model = Line
    extra = 0

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc', 'factory')
    inlines = [ChoiceInlineForWorkshop]

class ChoiceInlineForLine(admin.TabularInline ):
    model = Station
    extra = 0

class LineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'line_type', 'desc', 'workshop', 'department')
    inlines = [ChoiceInlineForLine]

class StationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc', 'line')
    #inlines = [ChoiceInlineForStation]

admin.site.register(Nation, NationAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Department, DepartmentAdmin)