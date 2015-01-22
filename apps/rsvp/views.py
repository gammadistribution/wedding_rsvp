from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from rsvp.models import Person


class RsvpWizardView(SessionWizardView):
    """Class based view for Form Wizard for RsvpAttendanceForm and
    RsvpPreferenceForm for Rsvp model. Creates page first for
    RsvpAttendanceForm and if attendance is True, redirect to second page for
    RsvpPreferenceForm and collect data for rest of model.
    """
    template_name = 'rsvp/attendance.html'

    def get_form(self, step=None, data=None, files=None):
        """Override get_form method of SessionWizardView.
        """
        form = super(RsvpWizardView, self).get_form(step, data, files)

        return form

    def done(self, form_list, **kwargs):
        """When form is complete redirect to personalized confirmation page.
        """
        # Must save data when done
        person = self.get_cleaned_data_for_step('0')['person']
        url = reverse('confirmation', kwargs={'slug': person.slug})
        return HttpResponseRedirect(url)


class ConfirmationView(DetailView):
    """Class based view for confirmation page of Rsvp form submission.
    Returns message thanking user for submitting Rsvp.
    """
    model = Person
    template_name = 'rsvp/confirmation.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        return super(ConfirmationView, self).get_context_data(**kwargs)
