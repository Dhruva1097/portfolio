from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import users

# Create your views here.
def home(req):
    return render(req,'index.html')

def portfolio(req):
    return render(req,'portfolio.html')

def contact(req):
    return render(req,'contact.html')

def signup(req):
    # if 'loggedin' not in req.session or req.session["loggedin"] != True:
    #     return redirect('/login')
    # req.POST.get('email').exists()
    invalid_pass = 'Passwords Do Not Match. Please ensure both passwords are identical and try again.'
    if not users.objects.filter(email=req.POST.get('email')).exists() and 'signup' in req.POST:
        if req.POST.get('password') == req.POST.get('confirm-password'):
            u = users(email=req.POST['email'],password=req.POST['password'])
            u.save()
            req.session["loggedin"] = False
            
            return redirect('/tools')
        else:
            return render(req,'signup.html',{'message':invalid_pass})
    else:
        return render(req,'signup.html',{'message':"Email already exists"})

def login(req):
    # if 'loggedin' not in req.session or req.session["loggedin"] != True:
    #     return redirect('/login')
    
    invalid_pass = 'Invalid Password'
    if 'login' in req.POST:
        email = req.POST.get('email')
        password = req.POST.get('password')
        user = users.objects.filter(email=email).first()
        
        if user.password == password:
            req.session["loggedin"] = True
            req.session['user_id'] = user.id
            return redirect('/tools')
        else:
            return render(req,'login.html',{'message':invalid_pass})
    else:
        return render(req,'login.html')

def logout_view(req):
    if req.session.get('loggedin'):
        del req.session['loggedin']
    return redirect('/login')

def terms(req):
    return render(req,'terms.html')