from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mark
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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
    fields = ['ref', 'loc', 'current_pic']

class MarkUpdate(UpdateView):
    model = Mark
    fields = ['ref', 'loc', 'current_pic']

class MarkDelete(DeleteView):
    model = Mark
    success_url = reverse_lazy('pics:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'pics/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data 
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            
            user = form.save(commit = False)

            # cleaned /normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password)
            if user is not None:
                
                if user.is_active:
                    login(request, user)
                    return redirect('pics:index')
        return render(request, self.template_name, {'form': form})
        
