from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Skills


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def relevance(request):
    return render(request, 'main/relevance.html')

def skills(request):
    skills_objects = Skills.objects.all()
    return render(request, 'main/skills.html', {'skills_objects': skills_objects})
