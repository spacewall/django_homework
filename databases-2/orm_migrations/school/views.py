from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {
        'object_list': Student.objects.all().order_by('group')
    }

    for item in context['object_list']:
        print(item.teachers)

    return render(request, template, context)
