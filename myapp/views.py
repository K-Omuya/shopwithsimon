from django.shortcuts import render,redirect

from myapp.models import Member


# Create your views here.
def index(request):
 if request.method == 'POST':
     if Member.objects.filter(
             fullname=request.POST['fullname'],
             email=request.POST['email'],
             username=request.POST['username'],
             password=request.POST['password']
     ).exists():
         member = Member.objects.get(
            fullname=request.POST['fullname'],
            email=request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password'],
         )
         return render(request,'index.html',{'members':member})
     else:
         return render(request,'login.html')
 else:
     return render(request,'login.html')


def landing_page(request):
    return render(request,'landing_page.html')
def login(request):
    return render(request,'login.html')
def sign_in(request):
    if request.method == "POST":
        members = Member(
            fullname=request.POST['fullname'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'sign_in.html')
