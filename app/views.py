from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Memorial,Photo
from django.shortcuts import get_object_or_404
from django import forms
from .forms import PhotoForm


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = Memorial
    context_object_name = 'memorial'
    template_name = 'app/bloglist.html'

class BlogDetailView(DetailView):
    model = Memorial
    context_object_name = 'memorial'
    template_name = 'app/blogdetail.html'

class BlogCreateView(CreateView):
    model = Memorial
    fields = ['user','firstname','lastname','dateofbirth','dateofdeath', 'biography','image']
    template_name = 'app/blogcreate.html'

class BlogUpdateView(UpdateView):
        model = Memorial
        fields = ['user', 'firstname', 'lastname', 'dateofbirth', 'dateofdeath', 'biography', 'image']
        template_name = 'app/blogupdate.html'

class BlogDeleteView(DeleteView):
    model = Memorial
    template_name = 'app/blogdelete.html'
    success_url = reverse_lazy('blogs')

class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'app/addphoto.html'

    def form_valid(self, form):
        memorial = get_object_or_404(Memorial, pk=self.kwargs['pk'])
        form.instance.memorial = memorial
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to a different URL after a successful form submission
        return reverse('blogsdetail', kwargs={'pk': self.object.memorial.pk})

