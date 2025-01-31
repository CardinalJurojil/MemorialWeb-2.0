from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView, UpdateView, DeleteView
from .models import CustomUser
from .forms import CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user  # Display the logged-in user's profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/profileupdate.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user  # Allow user to edit their own profile

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'registration/profiledelete.html'
    success_url = reverse_lazy('login')  # Redirect to login after deletion

    def get_object(self):
        return self.request.user  # Allow user to delete their own account