from django.urls import path
from events.views import create_event, events,event_details,event_update,event_delete,create_category,update_category,delete_category, dashboard,RoleDetails,Rsvp_event,Delete_participant

urlpatterns = [

    path('events/',events,name="events"),

    path('create-event/',create_event,name="create-event"),
    path('event-details/<int:id>/',event_details,name="event-details"),
    path('event-update/<int:id>/',event_update,name="event-update"),
    path('event-delete/<int:id>/',event_delete,name="event-delete"),

    path('create-category/',create_category,name="create-category"),
    path('update-category/<int:id>/',update_category,name="update-category"),
    path('delete-category/<int:id>/',delete_category,name="delete-category"),
    
    path('dashboard/',dashboard,name="dashboard"),
    path('role-details/',RoleDetails,name="role-details"),
    path('rsvp-event/<int:event_id>/',Rsvp_event, name="rsvp-event"),
    path('delete-participant/<int:event_id>/<int:participant_id>',Delete_participant, name="delete-participant"),
]
