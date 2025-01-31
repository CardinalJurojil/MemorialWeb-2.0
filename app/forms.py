from django import forms
from .models import Photo,Message

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

