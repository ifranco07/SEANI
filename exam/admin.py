from django.contrib import admin
from .models import Stage, Exam, ExamModule

# Register your models here.
admin.site.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['stage', 'month', 'year']
    
class ExamModuleInLine(admin.TabularInline):
    model = ExamModule
    extra = 1
    
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'career']
    inlines = [ExamModuleInLine]