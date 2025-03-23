from django.shortcuts import render

# Create your views here.

def rohit(req):
    return render(req, 'player/hitman.html')
