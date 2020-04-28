from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import BlogUser, Document


class CreateBlogUserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = BlogUser
        fields = ['username', 'password', 'confirm_password', 'biography',]

    def clean(self):
        # Call the original clean method before doing our own stuff
        cleaned_data = super(CreateBlogUserModelForm, self).clean()

        # Get the values
        password = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirm_password')

        # Make sure they're the same
        if password != confirmed_password:
            raise forms.ValidationError({'password': 'Passwords do not match',})

        # Return the original cleaned data
        return cleaned_data


class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'document_1_name', 'document_1', 'document_1_desc',
                  'document_2_name', 'document_2', 'document_2_desc',]

