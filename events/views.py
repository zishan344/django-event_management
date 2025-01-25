from django.shortcuts import render, redirect
from .models import Event,Participant,Category
from django.http import HttpResponse
from .form import CategoryModelForm, EventModelForm , ParticipantModelForm
from django.contrib import messages

def showHome (request):
    return render(request,'home/home.html')

def create_category(request):
    pass
def create_event(request):
    create_event_form = EventModelForm()
    if request.method == "POST":
        if "submit_event" in request.POST:
            create_event_form = EventModelForm(request.POST)
            if create_event_form.is_valid():
                create_event_form.save()
                messages.success(request,"event created successfully")
                return redirect("create-event")  
    context = {
        "create_event_form": create_event_form,
    }
    return render(request, "form/create_event.html", context)

def event_update(request,id):
    event = Event.objects.get(id=id)
    create_event_form = EventModelForm(instance=event)
    print(create_event_form.initial)
    if request.method == 'POST':
        create_event_form = EventModelForm(request.POST,instance=event)
        if create_event_form.is_valid():
            event = create_event_form.save()
            messages.success(request, "Event updated successfully")
            return redirect('event-update',id)
    context={
        "create_event_form": create_event_form
    }
    return render(request,"form/create_event.html",context)

# delete event
def event_delete(request,id):
    if request.method == "POST":
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request,'Event deleted successfully')
        return redirect('events')
def attend_event():
    pass

def events(request):
    totalEvent = Event.objects.all()
    context={
        'totalEvent':totalEvent
    }
    return render(request, 'events.html', context)


# event details
def event_details(request,id):
    event = Event.objects.get(id=id)
    print(event)
    context={
        'event':event
    }
    return render(request, 'event_details.html',context)






def events_form(request):
    """Handle events request"""
    category_form = CategoryModelForm()
    event_create_form = EventModelForm()
    participant_create_form = ParticipantModelForm()

    if request.method == "POST":
        if "submit_category" in request.POST:
            category_form = CategoryModelForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect("events-form")  
        elif "submit_event" in request.POST:
            event_create_form = EventModelForm(request.POST)
            if event_create_form.is_valid():
                event_create_form.save()
                return redirect("events")  
        elif "submit_participant" in request.POST:
            participant_create_form = ParticipantModelForm(request.POST)
            if participant_create_form.is_valid():
                participant_create_form.save()
                return redirect("events") 
    context = {
        "category_form": category_form,
        "event_create_form": event_create_form,
        "participant_create_form": participant_create_form,
    }
    return render(request, "test.html", context)