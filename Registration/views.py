from django.shortcuts import render
from .models import Registration
def RegistrationCourse(request):
    n = ''
    if request.method == "POST":
        n = request.POST.get("name")
        fn = request.POST.get("fname")
        st = request.POST.get("study")
        sub =request.POST.get("subject")
        dat = request.POST.get("date")
        cell = request.POST.get("cellno")
        add = request.POST.get("address")
        exe = Registration(name = n, fname =fn, study = st, course =sub,registration_d =dat, contact = cell, address = add)# here variable name is database name
        exe.save();
        n = "thank you for enroll to itself"
    return render(request,"abc.html",{'msg1':n})

# Create your views here.
