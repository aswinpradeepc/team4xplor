from django.shortcuts import render

# Create your views 

def conductor_login(request):
    return render(request, 'conductor/login.html')

def ticket_view(request):
    return render(request, 'conductor/ticket.html')