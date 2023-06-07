from django.shortcuts import render

from .forms import CustomerUserForm

# Create your views here.


def register(request):
    
    form = CustomerUserForm()
    return render(request, 'registration/register.html', {'form': form})
