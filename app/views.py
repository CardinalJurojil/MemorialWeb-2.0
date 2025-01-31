from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils.translation.template import context_re
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Memorial, Photo, Tag, Message
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import PhotoForm, MessageForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class MemorialListView(ListView):
    model = Memorial
    context_object_name = 'memorial'
    template_name = 'app/Memorial/memoriallist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q','')
        if query:
            context['memorial'] = Memorial.objects.filter( Q(firstname__icontains=query) | Q(lastname__icontains=query))
        else:
            context['memorial'] = Memorial.objects.all()
        context['search query'] = query
        return context

class MemorialDetailView(DetailView):
    model = Memorial
    template_name = 'app/Memorial/memorialdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.all()  # Get all messages related to this memorial
        return context

class MemorialCreateView(CreateView):
    model = Memorial
    fields = ['user','firstname','lastname','dateofbirth','dateofdeath', 'biography', 'tags','image']
    template_name = 'app/Memorial/memorialcreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        context['tags'] = Tag.objects.all()

        return context

class MemorialUpdateView(UpdateView):
        model = Memorial
        fields = ['user', 'firstname', 'lastname', 'dateofbirth', 'dateofdeath', 'biography', 'image']
        template_name = 'app/Memorial/memorialupdate.html'

class MemorialDeleteView(DeleteView):
    model = Memorial
    template_name = 'app/Memorial/memorialdelete.html'
    success_url = reverse_lazy('Memorial')


#PHOTO

class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'app/Photo/addphoto.html'

    def form_valid(self, form):
        memorial = get_object_or_404(Memorial, pk=self.kwargs['pk'])
        form.instance.memorial = memorial
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to a different URL after a successful form submission
        return reverse('Memorialdetail', kwargs={'pk': self.object.memorial.pk})

class PhotoUpdateView(UpdateView):
        model = Photo
        fields = ['image']
        template_name = 'app/Photo/photoupdate.html'

        def get_queryset(self):
            # Get the memorial_pk from the URL
            memorial_pk = self.kwargs['memorial_pk']
            # Return the queryset filtered by the memorial
            return Photo.objects.filter(memorial__pk=memorial_pk)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['memorial'] = get_object_or_404(Memorial, pk=self.object.memorial.pk)
            return context

        def get_success_url(self):
            return reverse('Memorialdetail', kwargs={'pk': self.object.memorial.pk})

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'app/Photo/photodelete.html'

    def get_success_url(self):
        # Redirect to the correct 'memorial_detail' named pattern
        return reverse_lazy('Memorialdetail', kwargs={'pk': self.kwargs['memorial_pk']})



#MESSAGE
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']
    template_name = 'app/Message/messagecreate.html'

    def form_valid(self, form):
        form.instance.memorial_id = self.kwargs['pk']  # Assign the memorial ID
        form.instance.user = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Memorialdetail', kwargs={'pk': self.kwargs['pk']})

class MessageUpdateView(UpdateView):
    model = Message
    fields = ['content']
    template_name = 'app/Message/messageupdate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the memorial object to the context using the `memorial_pk` from the URL
        context['memorial'] = get_object_or_404(Memorial, pk=self.kwargs['memorial_pk'])
        return context

    def get_success_url(self):
        # Redirect to the `memroial_detail` view after updating the message
        return reverse_lazy('Memorialdetail', kwargs={'pk': self.kwargs['memorial_pk']})

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'app/Message/messagedelete.html'

    def get_object(self):

        return get_object_or_404(Message, pk=self.kwargs['pk'], memorial__pk=self.kwargs['memorial_pk'])

    def get_success_url(self):
        # Redirect to the memorial's detail page after deleting the message
        return reverse_lazy('Memorialdetail', kwargs={'pk': self.kwargs['memorial_pk']})




