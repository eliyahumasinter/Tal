from django.shortcuts import render, redirect
from .models import Email, Card, Event
from django.contrib import messages
import datetime
# Create your views here.


def home(request):
    cards = Card.objects.all().order_by('-date_posted')
    context = {'cards': cards}
    return render(request, 'home/home.html', context)


def donate(request):
    return render(request, 'home/donate.html')


def about(request):
    return render(request, 'home/about.html')


def events(request):
    # only send objects that dates haven't passed yet
    today = datetime.date.today()
    events = Event.objects.all().order_by(
        'date').filter(date__range=[today, "2050-1-1"])
    context = {'events': events}
    context['events'] = [
        {
            'title': obj.title,
            'subtitle': obj.subtitle,
            'date': obj.date,
            'address': obj.address
        }
        for obj in events
    ]
    return render(request, 'home/events.html', context=context)


def getemail(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Email.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 "This email has already been registered")
            return redirect("home")

        newemail = Email(email=email)
        newemail.save()
    messages.add_message(request, messages.SUCCESS,
                         'Thank you for subscribing!')
    return redirect('home')
