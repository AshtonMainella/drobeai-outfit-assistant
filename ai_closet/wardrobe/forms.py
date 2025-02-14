from django import forms
from .models import ClothingItem
from .models import Profile

class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['name', 'category', 'image']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']