"""Forms of the project."""
from django import forms
from things.models import Thing

# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['created_at']

    # Customize the widgets for specific fields
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 120}))
    quantity = forms.IntegerField(widget=forms.NumberInput)
