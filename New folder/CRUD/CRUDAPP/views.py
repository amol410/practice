from django.shortcuts import render, redirect
from .models import User
from .forms import StudentRegistration

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    
    stud = User.objects.all()
        
    return render(request, "CRUDAPP/addandshow.html", {'form':fm, 'stu':stud})

def updatedata(request, pk):
    if request.method == 'POST':
        pi = User.objects.get(pk=pk)
        fm = StudentRegistration(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=pk)
        fm = StudentRegistration(instance=pi)

    return render(request, "CRUDAPP/updatestudent.html", {'form':fm}  )


def delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        user.delete()
        return redirect("add_show")
    
        
