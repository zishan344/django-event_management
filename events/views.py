from django.shortcuts import render, redirect,get_object_or_404
from .models import Event,Category
from django.http import HttpResponse
from .form import CategoryModelForm, EventModelForm
from django.contrib import messages
from django.db.models import Count,Q
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
def showHome (request):
    return render(request,'home/home.html')

def dashboard(request):
    today_date = now().date()
    events = Event.objects.select_related('category').all()
    categorys = Category.objects.prefetch_related('event_set').all()
    total_events = events.count()
    todays_events = events.filter(date=today_date)
    upcoming_events = events.filter(date__gt=today_date).count()
    past_events = events.filter(date__lt=today_date).count()
    groups = Group.objects.all()
    users = User.objects.all()
    user_groups = users[4].groups.all()
    attendEvents = Event.objects.filter(participant=request.user)
    if user_groups.exists():
        print("User group:", user_groups[0])
    else:
        print("User has no group")
    context = {
        'events': events,
        'total_events': total_events,
        'total_participants': 10,
        'todays_events': todays_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'categorys': categorys,
        'groups':groups,
        'users':users,
        'attendEvents': attendEvents
    }
    return render(request,'dashboard/dashboard.html',context)

def RoleDetails(request):
    groups = Group.objects.all()
    return render(request, "dashboard/roleDetails.html",{"groups":groups})

def create_category(request):
    create_category_form = CategoryModelForm()
    if request.method == "POST":
        if "submit_category" in request.POST:
            create_category_form = CategoryModelForm(request.POST)
            if create_category_form.is_valid():
                create_category_form.save()
                messages.success(request,"Event Category created successfully")
                return redirect("create-category")  
    context = {
        "create_form": create_category_form,
        "form_title":"Create Category",
        "submit":"submit_category"
    }
    return render(request, "form/form.html", context)


def update_category(request, id):
    category = Category.objects.get(id=id)
    print("category field",category)
    create_category_form = CategoryModelForm(instance=category)
    
    if request.method == 'POST':
        create_category_form = CategoryModelForm(request.POST, instance=category)
        if create_category_form.is_valid():
            category = create_category_form.save()
            messages.success(request, "Category updated successfully")
            return redirect('dashboard')
    context = {
        "create_form": create_category_form,
        "form_title": "Update Category",
        "submit": "Update Category"
    }
    return render(request, "form/form.html", context)


def delete_category(request,id):
    if request.method == "POST":
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request,'category deleted successfully')
        return redirect('dashboard')

def create_event(request):
    create_event_form = EventModelForm()
    if request.method == "POST":
        if "submit_event" in request.POST:
            create_event_form = EventModelForm(request.POST,request.FILES)
            if create_event_form.is_valid():
                create_event_form.save()
                messages.success(request,"event created successfully")
                return redirect("create-event")  
    context = {
        "create_form": create_event_form,
        "form_title":"Create Event",
        "submit":"submit_event"
    }
    return render(request, "form/form.html", context)


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
        "create_form": create_event_form,
        "form_title":"Update Event",
        "submit":"update_event"
    }
    return render(request,"form/form.html",context)


# delete 
def event_delete(request,id):
    if request.method == "POST":
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request,'Event deleted successfully')
        return redirect('dashboard')


def events(request):
    totalEvent = Event.objects.all()
    
    # query parameters
    name_query = request.GET.get('name', None)
    location_query = request.GET.get('location', None)
    start_date_query = request.GET.get('start_date', None)
    end_date_query = request.GET.get('end_date', None)
    
    category_query = request.GET.get('category_query', None)
    print(f"category querysss {category_query}")
    # filter
    if name_query:
        totalEvent = totalEvent.filter(name__icontains=name_query)
    
    if location_query:
        totalEvent=totalEvent.filter(location__icontains=location_query)
    
    if start_date_query and end_date_query:
        try:
            start_date =datetime.strptime(start_date_query,"%Y-%m-%d")
            end_date =datetime.strptime(end_date_query,"%Y-%m-%d")
            totalEvent = totalEvent.filter(Q(date__gte=start_date) if start_date else Q() & Q(date__lte=end_date) if end_date else Q())
        except ValueError:
            pass
    
    if category_query:
        if category_query =="all":
            totalEvent = Event.objects.all()
        else:
            totalEvent = totalEvent.filter(category__id__in=category_query.split(','))
    context= {
        'totalEvent': totalEvent,
        'categorys':Category.objects.all(),
    }
    return render(request, 'AllEvents/events.html', context)


# event details
def event_details(request,id):
    event = Event.objects.all().get(id=id)
    participants=["rakib","rahim","karim","dummy bossa"]
    context={
        'event':event,
        'participants':participants
    }
    return render(request, 'AllEvents/event_details.html',context)

@login_required
def Rsvp_event(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user not in event.participant.all():
        event.participant.add(request.user)
        return redirect('events')
    return messages.error(request,"Already RSVP'd")
