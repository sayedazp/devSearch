from django.forms import ModelForm
from .models import Project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link',
                  'source_link', 'tags']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class':'input'})
