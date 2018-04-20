from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mark
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name="pics/index.html"
    context_object_name = "all_marks"
    def get_queryset(self):
        return Mark.objects.all()

class DetailView(generic.DetailView):
    
    template_name = 'pics/detail.html'
    model = Mark

class MarkCreate(CreateView):
    model = Mark
    fields = ['ref', 'loc']