from django.shortcuts import render,redirect
from .models import new_user
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user= new_user.objects.filter(username=username,password=password)
        if user:
            user_details=new_user.objects.get(username=username,password=password)
            id=user_details.id
            username_user=user_details.username
            request.session['id']=id
            request.session['username'] = username_user
            return redirect('home')
    return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    id=request.session['id']
    username=request.session['username']
    return render(request, 'home.html',{'id':id,'name': username})
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    del request.session["id"]
    return render(request,'login.html')

