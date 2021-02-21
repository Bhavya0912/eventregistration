from django.shortcuts import render
from .models import Participant

# Create your views here.
def home(request):
    context = {}
    return render(request, 'event/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.institution = request.POST.get('institution','-')

        if len(Participant.objects.all()) > 15:
            return render(request, 'event/failed.html', context)
        else:
            p1.save()
            return render(request, 'event/success.html', context)

        if request.method  == 'GET':
            context['username'] = ''
            context['email'] = ''
            context['phone'] = ''
            context['institution'] = ''

    return render(request, 'event/register.html', context)

def participants(request):
    context = {}
    
    context['participants'] = Participant.objects.all()
    return render(request, 'event/participants.html', context)

# Create your views here.
