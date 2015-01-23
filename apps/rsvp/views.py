from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from rsvp.models import Person, Rsvp


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
        """Using data gained from both steps, create and save
        instance of model rsvp.models.Rsvp.
        """
        person = Person.objects.get(email=cleaned_data['email'])
        meal_preference = cleaned_data['meal_preference']
        rsvp = Rsvp.objects.create(person=person,
                                   attendance=cleaned_data['attendance'],
                                   guests=cleaned_data['guests'],
                                   meal_preference=meal_preference)

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


class ConfirmationView(ListView):
    """Class based view for confirmation page of Rsvp form submission.
    Returns message thanking user for submitting Rsvp.
    """
    model = Person
    template_name = 'rsvp/confirmation.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        return super(ConfirmationView, self).get_context_data(**kwargs)
