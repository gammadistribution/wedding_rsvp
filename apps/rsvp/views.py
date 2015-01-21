from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import SessionWizardView


class RsvpWizard(SessionWizardView):
    """Class based view for Form Wizard for RsvpAttendanceForm and
    RsvpPreferenceForm for Rsvp model. Creates page first for
    RsvpAttendanceForm and if attendance is True, redirect to second page for
    RsvpPreferenceForm and collect data for rest of model.
    """
    def done(self, form_list, **kwargs):
        print(form_list)
        return HttpResponseRedirect('')
