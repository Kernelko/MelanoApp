from django.shortcuts import render,get_object_or_404
from .models import Mark, Picture_file
# Create your views here.

def index(request):
    all_marks = Mark.objects.all()
    return render(request, 'pics/index.html', { 'all_marks' : all_marks, })

def detail(request,mark_id):
    mark =get_object_or_404(Mark, pk=mark_id)
    return render(request, 'pics/detail.html', {'mark':mark})

