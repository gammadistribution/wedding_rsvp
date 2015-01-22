from django.conf.urls import patterns, url
from rsvp.forms import RsvpAttendanceForm, RsvpPreferenceForm
from rsvp import views


regex = {'confirmation':
         r'attendance/(?P<slug>[^/]+)$'}


urlpatterns = patterns('',
                       url(r'attendance$',
                           views.RsvpWizardView.as_view([RsvpAttendanceForm,
                                                         RsvpPreferenceForm]),
                           name='rsvp_form'),
                       url(regex['confirmation'],
                           views.ConfirmationView.as_view(),
                           name='confirmation')
                       )
