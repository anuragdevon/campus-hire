from django.contrib import admin
from .models import JobPosting, Company, Student


@admin.register(Student)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'roll_number')
    list_filter = ('status',)

@admin.register(Company)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    list_filter = ('name',)

@admin.register(JobPosting)
class JobOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status')
    list_filter = ('company','title', 'status')


