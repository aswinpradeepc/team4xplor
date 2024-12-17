from django.shortcuts import render

# Create your views 

def conductor_login(request):
    return render(request, 'conductor/login.html')

