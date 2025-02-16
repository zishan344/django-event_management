from datetime import datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import Group
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import Q
from .models import Event,Category
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from .form import CategoryModelForm, EventModelForm
from users.views import is_admin,is_organizer,is_participant
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth import get_user_model

User = get_user_model()

def showHome (request):
    return render(request,'home/home.html')

@login_required(login_url="sign-in")
def dashboard(request):
    today_date = now().date()
    current_month = today_date.month
    current_year = today_date.year
    events = Event.objects.select_related('category').all()
    categorys = Category.objects.prefetch_related('event_set').all()
    total_events = events.count()
    todays_events = events.filter(date=today_date)
    upcoming_events = events.filter(date__gt=today_date).count()
    past_events = events.filter(date__lt=today_date).count()
    groups = Group.objects.all()
    users = User.objects.all()
    attendEvents = Event.objects.filter(participant=request.user)
    total_participants = User.objects.filter(rsvp_event__isnull=False).distinct().count()
    new_this_month = events.filter(date__month=current_month, date__year=current_year).count()
    previous_month = events.filter(
        date__month=(current_month - 1) if current_month > 1 else 12,
        date__year=(current_year if current_month > 1 else current_year - 1)
    ).count()
    next_month = events.filter(
        date__month=(current_month + 1) if current_month < 12 else 1,
        date__year=(current_year if current_month < 12 else current_year + 1)
    ).count()
    last_month = previous_month
    context = {
        'events': events,
        'total_events': total_events,
        'total_participants': total_participants,
        'todays_events': todays_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'categorys': categorys,
        'groups':groups,
        'users':users,
        'attendEvents': attendEvents,
        'new_this_month': new_this_month,
        'previous_month': previous_month,
        'next_month': next_month,
        'last_month': last_month
    }
    return render(request,'dashboard/dashboard.html',context)



@login_required(login_url="sign-in")
@user_passes_test(is_admin, login_url="no-permission")
def RoleDetails(request):
    groups = Group.objects.all()
    return render(request, "dashboard/roleDetails.html",{"groups":groups})

class CreateCategory(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required ="events.add_category"
    login_url ='sign-in'
    model = Category
    form_class = CategoryModelForm
    template_name = "form/form.html"
    success_url=reverse_lazy('create-category')
    def get_context_data(self, **kwargs):
        kwargs['submit']="submit_category"
        kwargs['form_title']="Create Category"
        kwargs['submitTitle']="Create"
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        response= super().form_valid(form)
        messages.success(self.request,"Event Category created successfully")
        return response

@login_required(login_url="sign-in")
@permission_required("events.change_category",raise_exception=True,login_url='no-permission')
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

@login_required(login_url="sign-in")
@permission_required("events.delete_category",raise_exception=True,login_url='no-permission')
def delete_category(request,id):
    if request.method == "POST":
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request,'category deleted successfully')
        return redirect('dashboard')

class CreateEvent(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required ='events.add_event'
    login_url = 'sign-in'
    model = Event
    form_class= EventModelForm
    template_name = 'form/form.html'
    success_url= reverse_lazy('create-event')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = 'Create Event'
        context["sbmit"] = 'submit_event'
        return context
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"event created successfully")
        return response
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,"Your form have some problem. This is invalid request. Please try again")
        return response

class EventUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    print("event updating start")
    permission_required ='events.change_event'
    login_url = 'sign-in'
    model = Event
    pk_url_kwarg = 'id'
    form_class= EventModelForm
    template_name = 'form/form.html'
    success_url= reverse_lazy('dashboard')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = 'Update Event'
        context["sbmit"] = 'update_event'
        context["submitTitle"] = 'update'
        return context

# delete 
@login_required(login_url="sign-in")
@permission_required("events.delete_event",raise_exception=True,login_url='no-permission')
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

class EventListView(ListView):
    model = Event
    template_name = "AllEvents/events.html" 
    context_object_name = "totalEvent"

    def get_queryset(self):
        queryset = Event.objects.all()
        name_query = self.request.GET.get("name", None)
        location_query = self.request.GET.get("location", None)
        start_date_query = self.request.GET.get("start_date", None)
        end_date_query = self.request.GET.get("end_date", None)
        category_query = self.request.GET.get("category_query", None)

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)

        if location_query:
            queryset = queryset.filter(location__icontains=location_query)

        if start_date_query and end_date_query:
            try:
                start_date = datetime.strptime(start_date_query, "%Y-%m-%d")
                end_date = datetime.strptime(end_date_query, "%Y-%m-%d")
                queryset = queryset.filter(Q(date__gte=start_date) & Q(date__lte=end_date))
            except ValueError:
                pass

        if category_query:
            if category_query.lower() == "all":
                queryset = Event.objects.all()
            else:
                queryset = queryset.filter(category__id__in=category_query.split(","))

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context
class EventDetails(LoginRequiredMixin,DetailView):
    login_url = 'sign-in'
    model = Event
    template_name ='AllEvents/event_details.html'
    pk_url_kwarg = 'id'	

@login_required(login_url="sign-in")
@user_passes_test(is_participant,login_url='no-permission')
def Rsvp_event(request,event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user not in event.participant.all():
        event.participant.add(request.user)
        return redirect('events')
    return messages.error(request,"Already RSVP'd")

@login_required(login_url="sign-in")
@user_passes_test(is_admin,login_url="no-permission")
def Delete_participant(request,event_id,participant_id):
    event = get_object_or_404(Event, id=event_id)
    participant = get_object_or_404(User, id=participant_id)
    if participant in event.participant.all():
        event.participant.remove(participant)
        return redirect('event-details',id=event.id)
    return redirect('event-details',id=event.id)
