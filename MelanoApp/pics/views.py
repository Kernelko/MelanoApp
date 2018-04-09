from django.shortcuts import render,get_object_or_404
from .models import Mark, Picture_file
# Create your views here.

def index(request):
    all_marks = Mark.objects.all()
    return render(request, 'pics/index.html', { 'all_marks' : all_marks, })

def detail(request,mark_id):
    mark =get_object_or_404(Mark, pk=mark_id)
    return render(request, 'pics/detail.html', {'mark':mark})

def cancerous(request,mark_id):
    mark =get_object_or_404(Mark, pk=mark_id)
    try:
        selected_picture = mark.picture_file_set.get(pk=request.POST['picture'])
    except (KeyError, Picture_file.DoesNotExist):
        return render(request, 'pics/detail.html',{ 'mark': mark,
        "error_message": "You did not select a valid picture",
        })
    else:
        selected_picture.is_cancerous = True
        selected_picture.save()
        return render(request, 'pics/detail.html', {'mark': mark})
