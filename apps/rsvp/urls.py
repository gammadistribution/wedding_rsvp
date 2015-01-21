from django.conf.urls import patterns, url
from rsvp.forms import RsvpAttendanceForm, RsvpPreferenceForm
from rsvp import views


urlpatterns = patterns('',
                       url(r'^$',
                           views.RsvpWizard.as_view([RsvpAttendanceForm,
                                                     RsvpPreferenceForm]),
                           name='rsvp_form'),
                       )
