from django import forms

class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField(max_length=254)
     