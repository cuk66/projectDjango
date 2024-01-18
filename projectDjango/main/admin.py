from django.contrib import admin
from .models import Relevance
from .models import Skills
from .models import Geography
from .models import Content
from .models import ImageUpload


# Register your models here.
class RelevanceDisplay(admin.ModelAdmin):
    list_display = ('graph_salary_level', 'graph_num_vacancy', 'table')


admin.site.register(Relevance, RelevanceDisplay)


class SkillsDisplay(admin.ModelAdmin):
    list_display = ('table_name', 'table', 'graph_skills')


admin.site.register(Skills, SkillsDisplay)


class GeographyDisplay(admin.ModelAdmin):
    list_display = ('graph_salary_level_by_city', 'graph_vacancy_fraction_by_city', 'table')


admin.site.register(Geography, GeographyDisplay)

admin.site.register(Content)

admin.site.register(ImageUpload)
