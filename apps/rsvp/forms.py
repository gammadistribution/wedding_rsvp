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
    attendance = forms.BooleanField(label='Attendance', required=False)

    def is_valid(self):
        """Check if the form is valid. Run normal checks then see if Person
        has already filled out Rsvp before. If Person exists, then form is
        not valid and should return message that Person already returned
        Rsvp.
        """
        valid = super(RsvpAttendanceForm, self).is_valid()

        try:
            models.Person.objects.get(self.cleaned_data['email'])
            valid = False
        except models.Person.DoesNotExist:
            valid = True

        return valid


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
