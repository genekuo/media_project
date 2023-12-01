from django import forms

#class UploadForm(forms.Form):
#    file_upload = forms.ImageField()

from .models import ExampleModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = "__all__"
