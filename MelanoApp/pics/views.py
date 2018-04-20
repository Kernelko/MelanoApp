from django.views import generic
from .models import Mark

class IndexView(generic.ListView):
    template_name="pics/index.html"
    context_object_name = "all_marks"
    def get_queryset(self):
        return Mark.objects.all()

class DetailView(generic.DetailView):
    model = Mark
    template = "pics/detail.html"
