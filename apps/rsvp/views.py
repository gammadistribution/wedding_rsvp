from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import SessionWizardView


class RsvpWizardView(SessionWizardView):
    """Class based view for Form Wizard for RsvpAttendanceForm and
    RsvpPreferenceForm for Rsvp model. Creates page first for
    RsvpAttendanceForm and if attendance is True, redirect to second page for
    RsvpPreferenceForm and collect data for rest of model.
    """
    template_name = 'rsvp/attendance.html'

    def done(self, form_list, **kwargs):
        print(form_list)
        return HttpResponseRedirect('redirect-page')