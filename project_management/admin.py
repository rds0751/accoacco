from django.contrib import admin
from ra.admin.admin import ra_admin_site

# Register your models here.
from django.contrib.auth.models import User
from utility.models import  UserProfile,Company,CompanyBranch,PredfinedPointsRule
from project_management.models import  Project,ProjectManager,Task,TaskPerformed,TaskPerformedReport,OverTime
#from hr.models import Employee_achievement


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1    

class ProjectManagerInline(admin.TabularInline):
    model = ProjectManager
    extra = 1    

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ProjectManagerInline,TaskInline]

class TaskPerformedReportInline(admin.TabularInline):
    model = TaskPerformedReport
    extra = 1    

class TaskPerformedAdmin(admin.ModelAdmin):
    model   = TaskPerformed
    inlines = [TaskPerformedReportInline]

class OverTimeAdmin(admin.ModelAdmin):
    model = OverTime    

ra_admin_site.register(Project, ProjectAdmin) 
ra_admin_site.register(TaskPerformed, TaskPerformedAdmin) 
ra_admin_site.register(OverTime, OverTimeAdmin)          