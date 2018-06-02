from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class AddBlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label="Description", widget=CKEditorWidget(attrs={'class':'form-control'}))
    class Meta:
        model = Blog
        fields = ('category', 'title', 'description', 'image')