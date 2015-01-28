from django import forms
from django.forms import ModelForm
from rsvp import models
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """Custom class for horizontal radio buttons. Set this as the renderer
    forms.RadioSelect to have the horizontal buttons.
    """
    def render(self):
        """Override RadioSelect renderer to make the buttons format
    horizontally.
        """
        return mark_safe('\n'.join(['{0}\n'.format(w) for w in self]))


class RsvpAttendanceForm(ModelForm):
    """This is part 1 of the form to submit for the Rsvp model. It will gather
    information about the person and attendance fields of the Rsvp model.
    """

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = models.Rsvp
        fields = ['first_name',
                  'last_name',
                  'email',
                  'attendance']
        widgets = {'attendance':
                   forms.RadioSelect(renderer=HorizontalRadioRenderer)}
        labels = {'attendance': 'Will you be joining us for the big day?'}

    def clean(self):
        """When cleaning data, check to see if email already submitted for
        person. If so, raise Validation error.
        """
        cleaned_data = super(RsvpAttendanceForm, self).clean()
        email = cleaned_data.get('email')

        try:
            models.Person.objects.get(email=email)
            message = 'An Rsvp has already been submitted for this email'
            message += ' address.'
            raise forms.ValidationError(message)
        except models.Person.DoesNotExist:
            pass


class RsvpPreferenceForm(ModelForm):
    """This is part 2 of the form to submit for the Rsvp model. It will gather
    information about the guests and meal_preference fields of the Rsvp model.
    This part of the form should only appear if the attendance option was
    selected as False.
    """
    music_preference = forms.CharField(required=False)

    class Meta:
        model = models.Rsvp
        fields = ['guests',
                  'meal_preference',
                  'music_preference']
        widgets = {'meal_preference':
                   forms.RadioSelect(renderer=HorizontalRadioRenderer)}
