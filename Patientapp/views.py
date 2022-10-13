from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import Patientreg,Question,Suggestion,Appointment,payment
from Clinicapp.models import ClinicReg,Clinicdet
from Doctorapp.models import Doctorreg,Medihis,Prescription
from Adminapp.models import Login,State,District,Place,Specialization,Account
from django.http import JsonResponse

# Create your views here.
def patienthome(request):
    context={}
    template=loader.get_template("patienthome.html")
    return  HttpResponse(template.render(context,request))

def patienttemp(request):
    context={}
    template=loader.get_template("patienttemp.html")
    return  HttpResponse(template.render(context,request))

def patientreg(request):
    if request.method=='POST':
        p=Patientreg()
        l=Login()
        name=request.POST.get("name")
        age = request.POST.get("age")
        gend = request.POST.get("gend")
        addr = request.POST.get("addr")
        state = request.POST.get("state")
        dist = request.POST.get("dist")
        place = request.POST.get("place")
        email = request.POST.get("email")
        mob = request.POST.get("mob")
        username = request.POST.get("uname")
        pwd = request.POST.get("pwd")

        p.Name=name
        p.Age=age
        p.Gender=gend
        p.Address=addr
        p.State=state
        p.District=dist
        p.Place=place
        p.Email=email
        p.Mobile=mob
        p.Uname=username
        p.Pswd=pwd
        p.save()
        l.Uname = username
        l.Pswd = pwd
        l.Utype = 'patient'
        l.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/patientreg';</script>")
    else:
        s=State.objects.all()
        context={'k':s}
        template=loader.get_template("patientreg.html")
        return HttpResponse(template.render(context,request))

def drop3(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = District.objects.filter(sid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def drop4(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Place.objects.filter(did=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def appointment(request):
    if request.method=='POST':
        a=Appointment()
        dist=request.POST.get("dist")
        loc=request.POST.get("loc")
        spec=request.POST.get("sp")
        clinic=request.POST.get("clinic")
        doctor=request.POST.get("dr")
        date=request.POST.get("date")
        time=request.POST.get("time")
        token=request.POST.get("token")
        uname = request.session["uname"]
        d = Patientreg.objects.get(Uname=uname)
        a.pid=d.id
        a.did=dist
        a.lid=loc
        a.spid=spec
        a.clid=clinic
        a.docid=doctor
        a.Date=date
        a.Time=time
        a.Token=token
        a.Status='pending'
        a.save()
        request.session["amount"]=250

        return HttpResponse("<script>alert('Appointment Successfull');window.location='/payment';</script>")
    else:
        d=District.objects.all()
        s=Specialization.objects.all()
        c=ClinicReg.objects.all()
        context={'k':d,'p':s,'r':c}
        template=loader.get_template("appointment.html")
        return  HttpResponse(template.render(context,request))

def app1(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Place.objects.filter(did=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def app2(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Doctorreg.objects.filter(clid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def queries(request):
    if request.method=='POST':
        q=Question()
        ques=request.POST.get("ques")
        uname = request.session["uname"]
        d = Patientreg.objects.get(Uname=uname)
        q.pid=d.id
        q.Ques=ques
        q.Status='pending'
        q.save()
        return HttpResponse("<script>alert('Question Added Successfully');window.location='/queries';</script>")
    else:
        context={}
        template=loader.get_template("queries.html")
        return  HttpResponse(template.render(context,request))

def suggestion(request):
    if request.method=='POST':
        s=Suggestion()
        sug=request.POST.get("sug")
        uname = request.session["uname"]
        d = Patientreg.objects.get(Uname=uname)
        s.pid=d.id
        s.Sugg=sug
        s.save()
        return HttpResponse("<script>alert('Suggestion Added Successfully');window.location='/sugg';</script>")
    else:
        context={}
        template=loader.get_template("suggestions.html")
        return  HttpResponse(template.render(context,request))

def viewapp(request):
    uname = request.session["uname"]
    d = Patientreg.objects.get(Uname=uname)
    a=Appointment.objects.raw("SELECT patientapp_patientreg.Name,patientapp_appointment.*,doctorapp_doctorreg.* FROM patientapp_patientreg INNER JOIN patientapp_appointment on patientapp_patientreg.id=patientapp_appointment.pid INNER JOIN doctorapp_doctorreg ON doctorapp_doctorreg.id=patientapp_appointment.docid WHERE patientapp_patientreg.id='%s'",[d.id])
    context = {'k':a}
    template = loader.get_template("viewappointment.html")
    return HttpResponse(template.render(context, request))

def cancel(request,id):
    a=Appointment.objects.get(id=id)
    a.delete()
    return HttpResponse("<script>alert('Appointment Cancelled');window.location='/viewapp';</script>")

def viewans(request):
    q=Question.objects.all()
    context = {'k':q}
    template = loader.get_template("viewanswers.html")
    return HttpResponse(template.render(context, request))

def viewmed(request):
    uname = request.session["uname"]
    d = Patientreg.objects.get(Uname=uname)
    m=Medihis.objects.raw("SELECT doctorapp_medihis.*,patientapp_patientreg.Name,doctorapp_doctorreg.DrName FROM doctorapp_medihis,doctorapp_doctorreg,patientapp_patientreg WHERE patientapp_patientreg.id=doctorapp_medihis.pid AND doctorapp_doctorreg.id=doctorapp_medihis.docid AND doctorapp_medihis.pid=%s",[d.id])
    context = {'k':m}
    template = loader.get_template("viewmedhis.html")
    return HttpResponse(template.render(context, request))

def search(request):
    c = ClinicReg.objects.all()
    context = {'k': c}
    template = loader.get_template("searchclinic.html")
    return HttpResponse(template.render(context, request))

def drp(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Clinicdet.objects.filter(clid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def viewpre(request):
    uname = request.session["uname"]
    d = Patientreg.objects.get(Uname=uname)
    p=Prescription.objects.raw("SELECT doctorapp_prescription.*,doctorapp_doctorreg.DrName FROM doctorapp_prescription,doctorapp_doctorreg WHERE doctorapp_doctorreg.id=doctorapp_prescription.docid and doctorapp_prescription.pid=%s",[d.id])

    context={'k':p}
    template=loader.get_template("viewprescription.html")
    return HttpResponse(template.render(context,request))

def phome(request):
    template = loader.get_template("paymenthome.html")
    context = {}
    return HttpResponse(template.render(context, request))
def paymentcon(request):

     cno = request.POST.get("cno")
     request.session["cno"] = cno
     sum = request.session["amount"]
     if (Account.objects.get(cno=cno)):
        x = Account.objects.get(cno=cno)
        context = {'sum': sum, 'card': x}
        template = loader.get_template("paymentcon.html")
        return HttpResponse(template.render(context, request))
     else:
        return HttpResponse("<script>alert('invalid card no');window.location='/payment';</script>")

def savepayment(request):

    uname=request.session["uname"]
    uid=Patientreg.objects.get(Uname=uname)
    p=payment()
    p.uid=uid.id
    p.amt=request.session["amount"]
    p.save()
    x = request.session["cno"]
    c = Account.objects.get(cno=x)
    c.amount=int(c.amount)-int(request.session["amount"])
    c.save()
    return HttpResponse("<script>alert('payment completed successfully');window.location='/patienthome';</script>")
def drp3(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Appointment.objects.filter(clid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)
def payment1(request):


    context = {}
    template = loader.get_template("payment.html")
    return HttpResponse(template.render(context, request))