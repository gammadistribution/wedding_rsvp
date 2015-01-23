from django import forms
from django.forms import ModelForm
from rsvp import models


class RsvpAttendanceForm(forms.Form):
    """This is part 1 of the form to submit for the Rsvp model. It will gather
    information about the person and attendance fields of the Rsvp model.
    """
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email Address', max_length=254)
    attendance = forms.BooleanField(label='Attendance')


class RsvpPreferenceForm(ModelForm):
    """This is part 2 of the form to submit for the Rsvp model. It will gather
    information about the guests and meal_preference fields of the Rsvp model.
    This part of the form should only appear if the attendance option was
    selected as False.
    """
    class Meta:
        model = models.Rsvp
        fields = ['guests',
                  'meal_preference']
