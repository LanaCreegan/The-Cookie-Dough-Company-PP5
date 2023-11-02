from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form for reviews """

    class Meta:
        model = Review
        fields = ['body',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)