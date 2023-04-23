from django.forms import ModelForm
from .models import Ticket
from django import forms
from ckeditor.widgets import CKEditorWidget

class TicketForm(ModelForm):
    description = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['host', 'participants']