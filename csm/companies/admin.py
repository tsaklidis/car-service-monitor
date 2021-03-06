from django.contrib import admin

from csm.companies.models import Company, Department, Garage


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('name', 'id')


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    model = Garage
    list_display = ('name', 'company')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_filter = ('company', )
    list_display = ('name', 'id', 'company', )

    # def employees_number(self, obj):
    #     return obj.employees.count()
    # employees_number.short_description = 'Number of Employees'
