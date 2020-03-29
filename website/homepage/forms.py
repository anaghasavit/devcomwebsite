from .import models
from django import forms

class writepost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','slug','body']

class EditPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','slug','body']