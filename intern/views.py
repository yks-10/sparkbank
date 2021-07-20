from django.shortcuts import render,redirect
from django.db import IntegrityError
from .forms import Intern
from .models import Customer

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'intern/home.html')
def transfer(request):
    if request.method == 'GET':
        return render(request,'intern/transfer.html', {'form':Intern()})
    else:
        try:
            form=Intern(request.POST)
            newintern =form.save(commit=False)
            newintern.save()
            return redirect('done')
        except ValueError:
            return render(request, 'intern/transfer.html', {'form': Intern()})


def done(request):
    return render(request, 'intern/done.html')


def customer(request):
    customer= Customer.objects.all
    return render(request, 'intern/customer.html',{'customer':customer})