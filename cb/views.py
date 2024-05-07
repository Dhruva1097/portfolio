from django.shortcuts import render
from .models import contacts

# Create your views here.
def cb_signup(req):
    records = contacts.objects.filter(client_id=req.session['user_id'])
    # records = contacts.objects.all()
    if req.method == "POST" and 'edit' not in req.POST:
        first_name = req.POST.get('floating_first_name')
        last_name = req.POST.get('floating_last_name')
        phone = req.POST.get('floating_phone')
        nickname = req.POST.get('floating_nickname')
        email = req.POST.get('floating_email')
        address = req.POST.get('floating_add')
        # avatar = req.POST.get('img')
        print(records)
        c = contacts(f_name = first_name,l_name = last_name,phone = phone,nickname = nickname,email = email,address = address, client_id=req.session['user_id'])
        c.save()
        return render(req,'cb.html')##,{'r':records} 
    
    elif req.method == "POST" and 'edit' in req.POST:
        phone = req.POST.get('efloating_phone')
        contact = contacts.objects.get(id=req.session['user_id'])

        contact.f_name = req.POST.get('efloating_first_name')
        contact.l_name = req.POST.get('efloating_last_name')
        contact.phone = req.POST.get('efloating_phone')
        contact.nickname = req.POST.get('efloating_nickname')
        contact.email = req.POST.get('efloating_email')
        contact.address = req.POST.get('efloating_add')

        contact.save()
        # avatar = req.POST.get('img')  
        # c = contacts(f_name = first_name,l_name = last_name,phone = phone,nickname = nickname,email = email,address = address)
        # c.save()
        return render(req,'cb.html',{'r':records}) 
    return render(req,'cb.html',{'r':records}) 


     