from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Skills


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def relevance(request):
    return render(request, 'main/relevance.html')


def skills(request):
    obj = Skills.objects.get(id=1)
    table_html = obj.table
    safe_html_code = mark_safe(table_html)
    return render(request, 'main/skills.html', {'table': safe_html_code})
