from django.shortcuts import render
from django.http import HttpResponse
from  django.template import loader
from.models import ClinicReg,Clinicdet
from Adminapp.models import Login,State,District,Place,Specialization
from django.http import JsonResponse
from Doctorapp.models import Doctorreg
# Create your views here.
def clinichome(request):
    context={}
    template=loader.get_template("clinichome.html")
    return HttpResponse(template.render(context,request))

def clinictemp(request):
    context={}
    template=loader.get_template("clinictemp.html")
    return HttpResponse(template.render(context,request))

def drreg(request):
    if request.method=='POST':
        d=Doctorreg()
        l=Login()
        name=request.POST.get("name")
        lic=request.POST.get("license")
        age=request.POST.get("age")
        gend=request.POST.get("gend")
        qual=request.POST.get("qual")
        sp=request.POST.get("sp")
        mob=request.POST.get("mob")
        email=request.POST.get("email")
        username=request.POST.get("uname")
        pswd=request.POST.get("pwd")
        uname = request.session["uname"]
        cl = ClinicReg.objects.get(Uname=uname)
        d.clid=cl.id
        d.DrName=name
        d.License=lic
        d.Age=age
        d.Gender=gend
        d.Qualification=qual
        d.Specialization=sp
        d.Mobile=mob
        d.Email=email
        d.Uname=username
        d.Pwd=pswd
        d.Status='pending'
        d.save()
        l.Uname=username
        l.Pswd=pswd
        l.Utype='doctor'
        l.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/clinichome';</script>")
    else:
        s=Specialization.objects.filter()
        context={'k':s}
        template=loader.get_template("doctorreg.html")
        return HttpResponse(template.render(context,request))

def clinicdet(request):
    if request.method=='POST':
        c=Clinicdet()
        state=request.POST.get("state")
        dist=request.POST.get("dist")
        place=request.POST.get("place")
        clinic=request.POST.get("clinic")
        spe=request.POST.get("spe")
        file=request.FILES["photo"]
        c.sid=state
        c.did=dist
        c.pid=place
        c.clid=clinic
        c.spid=spe
        c.Photo=file
        c.save()
        return HttpResponse("<script>alert('Clinic Details Added Successfully');window.location='/clinicdet';</script>")
    else:
        s=State.objects.all()
        c=ClinicReg.objects.all()
        sp=Specialization.objects.all()
        context={'k':s,'p':c,'q':sp}
        template=loader.get_template("clinicdet.html")
        return HttpResponse(template.render(context,request))

def det1(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = District.objects.filter(sid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def det2(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Place.objects.filter(did=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def reg(request):
    if request.method=='POST':
        c=ClinicReg()
        l=Login()
        cname=request.POST.get("cname")
        cont = request.POST.get("contact")
        oname = request.POST.get("oname")
        phno = request.POST.get("phno")
        addr = request.POST.get("addr")
        email = request.POST.get("email")
        dist = request.POST.get("dist")
        place = request.POST.get("place")
        loc = request.POST.get("loc")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        c.Name=cname
        c.Contact=cont
        c.Owner=oname
        c.OwnerContact=phno
        c.Address=addr
        c.Email=email
        c.District=dist
        c.Place=place
        c.Location=loc
        c.Uname=uname
        c.Pswd=pwd
        c.Status = 'pending'
        c.save()
        l.Uname=uname
        l.Pswd=pwd
        l.Utype='clinic'
        l.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location='/clinicreg';</script>")
    else:
        d=District.objects.all()
        context={'k':d}
        template=loader.get_template("clinicreg.html")
        return HttpResponse(template.render(context,request))

def drop1(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = Place.objects.filter(did=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

