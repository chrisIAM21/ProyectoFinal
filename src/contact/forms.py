from django import forms

class ContactForm(forms.Form):
    Nombre = forms.CharField()
    # phone = forms.CharField()
    Email = forms.EmailField(required = True)
    Mensaje = forms.CharField(widget=forms.Textarea ,  required = True)
