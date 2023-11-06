from django.shortcuts import render
from .models import Office

def home(request):
    n = ''
    if request.method == "POST":
        n = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        cont =request.POST.get("cellno")
        msg = request.POST.get("message")
        exe = Office(name = n, email =em, subject = sub, contact =cont, message = msg)# here variable name is database name
        exe.save();
        n = "Mahir Solution Team contact at your given number"
    return render(request,"homepage.html",{'msg':n})

#def Message(request):
 #   alldata = Office.objects.all()
    
  #  return render(request,"homepage.html")
        

# Create your views here. 
