from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():     #loop through all the fields in the form
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})      # add a class of input to the css
