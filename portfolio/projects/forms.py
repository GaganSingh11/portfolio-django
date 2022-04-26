from django.forms import ModelForm
from django import forms
from .models import Message

class ContactForm(ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Name"}))
    class Meta:
        model = Message
        fields = ['name','email','subject', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"class": "form-control","placeholder":"Name", "id":"contact-name","type":"text","name":"name","required":""})
        self.fields['email'].widget.attrs.update({"class": "form-control","placeholder":"Email", "id":"contact-email","type":"email", "name":"email","required":""})
        self.fields['subject'].widget.attrs.update({"class": "form-control","placeholder":"Subject", "id":"contact-sunject","type":"text", "name":"subject","required":""})
        self.fields['body'].widget.attrs.update({"class": "form-control","placeholder":"Message", "id":"contact-message", "name":"message", "rows":"5", "required":""})


        