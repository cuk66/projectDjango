from django.contrib import admin
from .models import Relevance

# Register your models here.
class RelevanceDisplay(admin.ModelAdmin):
    list_display = ('graph_salary_level', 'graph_num_vacancy', 'table')


admin.site.register(Relevance, RelevanceDisplay)

