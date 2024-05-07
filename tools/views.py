from django.shortcuts import render,redirect
from .models import Result

# Create your views here.
def toolsPage(req):
    if 'loggedin' not in req.session or req.session["loggedin"] != True:
        return redirect('/login')
    return render(req,'tools.html')

def studentRslt(req):
    if 'loggedin' not in req.session or req.session["loggedin"] != True:
        return redirect('/login')
    if req.method  == "POST" and not req.POST.get('getalldata') and req.POST.get('English') and req.POST.get('Hindi') and req.POST.get('Mathematics') and req.POST.get('Science') and req.POST.get('cs'):
        result = ''
        e = int(req.POST['English'])
        h = int(req.POST['Hindi'])
        m = int(req.POST['Mathematics'])
        s = int(req.POST['Science'])
        c = int(req.POST['cs'])

        total = int(req.POST['English']) + int(req.POST['Hindi']) + int(req.POST['Mathematics']) + int(req.POST['Science']) + int(req.POST['cs'])

        grade = 'A' if total > 400 else ('B' if total > 300 else 'C')
        if int(req.POST['English']) > 35 and int(req.POST['Hindi']) > 35 and int(req.POST['Mathematics']) > 35 and int(req.POST['Mathematics']) > 35 and int(req.POST['Science']) > 35 and int(req.POST['cs']) > 35:
            result = 'pass'
        else:
            result = 'fail'
            grade = 'D'
        perc = (total/500) * 100
        name = req.POST['name']
        data = {
            "total":total,
            "result":result,
            "perc":perc,
            "grade":grade,
        }
        r = Result(name = name,eng = e,hin = h,maths = m,sci = s,cs = c,total = total,perc = perc,res = result,grade = grade)
        r.save()
        return render(req,'studentRslt.html',data)
    elif req.method == 'POST' and req.POST.get('getalldata') and not req.POST.get('myid'):
        data = Result.objects.all()
        return render(req,'studentRslt.html',{'data':data})
    elif req.method  == "POST" and req.POST.get('myid'):
        member = Result.objects.get(id=req.POST['myid'])
        member.delete()
        
        data = Result.objects.all()
        return render(req,'studentRslt.html',{'data':data})
    elif req.method  == "POST" and req.POST.get('uEnglish') and req.POST.get('uHindi') and req.POST.get('uMathematics') and req.POST.get('uScience') and req.POST.get('ucs'):
        result = ''
        e = int(req.POST['uEnglish'])
        h = int(req.POST['uHindi'])
        m = int(req.POST['uMathematics'])
        s = int(req.POST['uScience'])
        c = int(req.POST['ucs'])

        total = int(req.POST['uEnglish']) + int(req.POST['uHindi']) + int(req.POST['uMathematics']) + int(req.POST['uScience']) + int(req.POST['ucs'])

        grade = 'A' if total > 400 else ('B' if total > 300 else 'C')
        if int(req.POST['uEnglish']) > 35 and int(req.POST['uHindi']) > 35 and int(req.POST['uMathematics']) > 35 and int(req.POST['uScience']) > 35 and int(req.POST['ucs']) > 35:
            result = 'pass'
        else:
            result = 'fail'
            grade = 'D'
        perc = (total/500) * 100
        name = req.POST['uname']
       
        member = Result.objects.get(id=req.POST['model_id'])
        member.name = name
        member.eng = e
        member.hin = h
        member.maths = m
        member.sci = s
        member.cs = c
        member.total = total
        member.perc = perc
        member.res = result
        member.grade = grade
        member.save()
        return render(req,'studentRslt.html')
    else:
        return render(req,'studentRslt.html')
    
def calc(req):
    if 'loggedin' not in req.session or req.session["loggedin"] != True:
        return redirect('/login')
    if req.method  == "POST":
        ans = eval(req.POST['data'])
        return render(req,'calc.html',{'data':ans})
    else:
        return render(req,'calc.html')

    