from django.shortcuts import render

def home(request):
    context = {'name': 'Django Developer'}
    return render(request, 'home.html', context)
