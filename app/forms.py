from django import forms
from .models import Entry1

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry1
        fields = ['title', 'description', 'attachment']
        labels = ['title':"Title",'description':"Description",'attachment':"Attach File"]