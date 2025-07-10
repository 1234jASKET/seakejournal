from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'journal/index.html')

def politique(request):
    return render(request, 'journal/politique.html')

def publicite(request):
    return render(request, 'journal/publicite.html')

def contact(request):
    return render(request, 'journal/contact.html')