from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory, modelformset_factory, BaseModelFormSet
from django.utils.translation import ugettext_lazy as _

from .models import BlogUser, Document, VoteRecord


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


class DocumentListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentListForm, self).__init__(*args, **kwargs)

        self.fields['title'].disabled = True
        self.fields['author'].disabled = True

    class Meta:
        model = Document
        fields = ['title', 'author', 'priority',]


class DocumentListFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Document.objects.all()


DocumentFormSet = modelformset_factory(model=Document, form=DocumentListForm, formset=DocumentListFormSet, extra=0)
