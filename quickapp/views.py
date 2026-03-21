from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm,RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, UserEventRegistration
from django.contrib import messages




def index(request):
    return HttpResponse(" Django is working! Hello from Quick Event")

'''
def index(request):
    events = Event.objects.all()
    return render(request, 'quickapp/index.html', {'events': events})
    '''


def index(request):
    events = Event.objects.all()
    registered_event_ids = []

    if request.user.is_authenticated:
        registered_event_ids = UserEventRegistration.objects.filter(
            user=request.user
        ).values_list('event_id', flat=True)

    return render(request, 'quickapp/index.html', {
        'events': events,
        'registered_event_ids': registered_event_ids
    })


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'quickapp/form.html', {'form': form, 'title': 'Add Event'})

def edit_event(request, pk):
    event = get_object_or_404(Event, id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm(instance=event)
    return render(request, 'quickapp/form.html', {'form': form, 'title': 'Edit Event'})

def delete_event(request, pk):
    event = get_object_or_404(Event, id=pk)
    event.delete()
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'quickapp/register.html', {'form': form})
    
@login_required
def register_event(request, id):
    event = get_object_or_404(Event, id=id)
    user = request.user
    
    # Check if already registered
    if UserEventRegistration.objects.filter(user=request.user, event=event).exists():
        messages.info(request, f"You have already registered for **{event.title}**.")
    else:
        UserEventRegistration.objects.create(user=request.user, event=event)
        messages.success(request, f"Successfully registered for **{event.title}**! Registration fee: ₹{event.fee}")

    return redirect('index') 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'quickapp/event_form.html', {'form': form})

# Update View
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm(instance=event)
    return render(request, 'quickapp/event_form.html', {'form': form, 'event': event})


# Delete view
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('index')
    return render(request, 'quickapp/event_confirm_delete.html', {'event': event})
# quickapp/views.py

def test(request):
    return render(request, 'quickapp/base.html')

def index(request):
    events = Event.objects.all()
    query = request.GET.get('q')
    if query:
        events = events.filter(name__icontains=query)
    return render(request, 'quickapp/index.html', {'events': events})






