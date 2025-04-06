from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class CodeForm(forms.Form):
    code = forms.CharField(max_length=6)