from django.urls import path
from events.views import create_event, events,events_form,event_details,event_update,event_delete

urlpatterns = [
    path('event-form/',events_form,name='events-form'),
    path('create-event/',create_event,name="create-event"),
    path('events/',events,name="events"),
    path('event-details/<int:id>/',event_details,name="event-details"),
    path('event-update/<int:id>/',event_update,name="event-update"),
    path('event-delete/<int:id>/',event_delete,name="event-delete"),
]
