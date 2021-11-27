from django import forms
from dashboard.models import Candidate

class AddCandidate(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ("name", "team", "slogan", "description")
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'team':forms.TextInput(attrs={'class':'form-control'}),
            'slogan':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'})
        }
