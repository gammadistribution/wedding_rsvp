from django.conf.urls import patterns, url
from rsvp.forms import RsvpAttendanceForm, RsvpPreferenceForm
from rsvp.views import ConfirmationView, RsvpWizardView
from rsvp.views import skip_wizard_step


regex = {'confirmation':
         r'attendance/(?P<slug>[^/]+)$'}


# Use this condition for FormWizard to skip from step 0 to complete.
condition = {'1': skip_wizard_step}


urlpatterns = patterns('',
                       url(r'attendance$',
                           RsvpWizardView.as_view([RsvpAttendanceForm,
                                                   RsvpPreferenceForm],
                                                  condition_dict=condition),
                           name='rsvp_form'),
                       url(regex['confirmation'],
                           ConfirmationView.as_view(),
                           name='confirmation'),
                       )
