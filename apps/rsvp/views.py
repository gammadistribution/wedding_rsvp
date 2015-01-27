from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from rsvp.models import Person, Rsvp


def skip_wizard_step(rsvp_wizard):
    """In RsvpWizardView, if 'attendance' on step 0 of the form is False,
    then skip step 1 and go to done portion of form.
    """
    cleaned_data = rsvp_wizard.get_cleaned_data_for_step('0') or {}

    attendance = cleaned_data.get('attendance', 'False')

    attendance = True if attendance == 'True' else False

    return attendance


class RsvpWizardView(SessionWizardView):
    """Class based view for Form Wizard for RsvpAttendanceForm and
    RsvpPreferenceForm for Rsvp model. Creates page first for
    RsvpAttendanceForm and if attendance is True, redirect to second page for
    RsvpPreferenceForm and collect data for rest of model.
    """
    template_name = 'rsvp/attendance.html'

    def create_person(self, cleaned_data):
        """Using data gained from step 0 of form wizard create and save
        instance of model rsvp.models.Person.
        """
        person = Person.objects.create(first_name=cleaned_data['first_name'],
                                       last_name=cleaned_data['last_name'],
                                       email=cleaned_data['email'])

        return person

    def create_rsvp(self, cleaned_data):
        """Using data gained from both steps, create and save instance of model
        rsvp.models.Rsvp. If step 1 was skipped, then return defaults for data
        that would have been gained in that step, i.e. return None for
        meal_preference, 0 for guests, and None for music_preference if step
        1 was skipped.
        """
        person = Person.objects.get(email=cleaned_data['email'])
        meal_preference = cleaned_data.get('meal_preference')
        guests = cleaned_data.get('guests', 0)
        music_preference = cleaned_data.get('music_preference')
        attendance = cleaned_data.get('attendance', 'False')
        attendance = True if attendance == 'True' else False
        rsvp = Rsvp.objects.create(person=person,
                                   attendance=attendance,
                                   guests=guests,
                                   meal_preference=meal_preference,
                                   music_preference=music_preference)

        return rsvp

    def done(self, form_list, **kwargs):
        """When form is complete redirect to personalized confirmation page.
        """
        cleaned_data = {}
        for form in form_list:
            cleaned_data.update(form.cleaned_data)

        person = self.create_person(cleaned_data)

        self.create_rsvp(cleaned_data)

        url = reverse('confirmation', kwargs={'slug': person.slug})

        return HttpResponseRedirect(url)


class ConfirmationView(DetailView):
    """Class based view for confirmation page of Rsvp form submission.
    Returns message thanking user for submitting Rsvp. The ListView is used
    as the first name and last name is not guaranteed to be unique.
    """
    model = Person
    template_name = 'rsvp/confirmation.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        return super(ConfirmationView, self).get_context_data(**kwargs)
