from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import State,District,Place,Specialization,Login,Bank,Branch,Account
from Clinicapp.models import ClinicReg
from Patientapp.models import Patientreg,Question,Suggestion
from Doctorapp.models import Doctorreg,Article
from django.http import JsonResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST.get("Username")
        pwd = request.POST.get("Password")
        if (Login.objects.filter(Uname=uname, Pswd=pwd)):
            l = Login.objects.filter(Uname=uname, Pswd=pwd)
            for i in l:
                Utype = i.Utype
            if Utype == 'admin':
                template = loader.get_template("admin.html")
                context = {}
                return HttpResponse(template.render(context, request))
            elif (Utype == 'clinic'):
                request.session["uname"] = uname
                d = ClinicReg.objects.get(Uname=uname)
                status = d.Status
                if (status == "approved"):
                    template = loader.get_template("clinichome.html")
                    context = {}
                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponse("<script>alert('Access Denied!!!!');window.location='/login'</script>")
            elif (Utype == 'patient'):
                request.session["uname"] = uname
                d = Patientreg.objects.get(Uname=uname)
                template = loader.get_template("patienthome.html")
                context = {}
                return HttpResponse(template.render(context, request))
            elif (Utype == 'doctor'):
                request.session["uname"] = uname
                d = Doctorreg.objects.get(Uname=uname)
                status = d.Status
                if (status == "approved"):
                    template = loader.get_template("doctorhome.html")
                    context = {}
                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponse("<script>alert('Access Denied!!!!');window.location='/login'</script>")
            else:
                return HttpResponse("<script>alert('Invalid User');window.location='/login'</script>")
    else:
        context={}
        template=loader.get_template("login.html")
        return HttpResponse(template.render(context,request))

def index(request):
    context={}
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))

def adminhome(request):
    context={}
    template=loader.get_template("admin.html")
    return HttpResponse(template.render(context,request))

def addstate(request):
    if request.method=='POST':
        s=State()
        state=request.POST.get("state")
        s.State=state
        s.save()
        return HttpResponse("<script>alert('State Added Successfully');window.location='/addstate';</script>")
    else:
        context={}
        template=loader.get_template("addstate.html")
        return HttpResponse(template.render(context,request))

def adddist(request):
    if request.method=='POST':
        d=District()
        state=request.POST.get("state")
        dist=request.POST.get("dist")
        d.sid=state
        d.district=dist
        d.save()
        return HttpResponse("<script>alert('District Added Successfully');window.location='/adddist';</script>")
    else:
        s=State.objects.all()
        context={'k':s}
        template=loader.get_template("adddistrict.html")
        return HttpResponse(template.render(context,request))

def addplace(request):
    if request.method=='POST':
        p=Place()
        state=request.POST.get("state")
        dist=request.POST.get("dist")
        place=request.POST.get("place")
        p.sid=state
        p.did=dist
        p.Place=place
        p.save()
        return HttpResponse("<script>alert('Place Added Successfully');window.location='/addplace';</script>")
    else:
        s=State.objects.all()
        context={'k':s}
        template=loader.get_template("addplace.html")
        return HttpResponse(template.render(context,request))

def drop(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        id = request.GET.get('q')
        l = District.objects.filter(sid=id).values()
        # users_list = list(framework)  # important: convert the QuerySet to a list object
        return JsonResponse(list(l), safe=False)

def specialization(request):
    if request.method=='POST':
        s=Specialization()
        cat=request.POST.get("cat")
        s.Category=cat
        s.save()
        return HttpResponse("<script>alert('Category Added Successfully');window.location='/specialization';</script>")
    else:
        context={}
        template=loader.get_template("specialization.html")
        return HttpResponse(template.render(context,request))

def approvedr(request):
    d=Doctorreg.objects.raw("SELECT doctorapp_doctorreg.*,clinicapp_clinicreg.Name,adminapp_specialization.Category from doctorapp_doctorreg,clinicapp_clinicreg,adminapp_specialization where clinicapp_clinicreg.id=doctorapp_doctorreg.clid AND adminapp_specialization.id=doctorapp_doctorreg.Specialization AND doctorapp_doctorreg.Status='pending'")
    context = {'k':d}
    template = loader.get_template("approvedoctor.html")
    return HttpResponse(template.render(context, request))

def draprve(request,id):
    r=Doctorreg.objects.get(id=id)
    r.Status='approved'
    r.save()
    return HttpResponse("<script>alert('Approved');window.location='/approvedr';</script>")

def approveclin(request):
    d=ClinicReg.objects.raw("SELECT clinicapp_clinicreg.*,adminapp_district.district,adminapp_place.Place FROM clinicapp_clinicreg,adminapp_district,adminapp_place WHERE adminapp_district.id=clinicapp_clinicreg.District AND adminapp_place.id=clinicapp_clinicreg.Place and clinicapp_clinicreg.Status='pending'")
    context = {'k':d}
    template = loader.get_template("approveclinic.html")
    return HttpResponse(template.render(context, request))

def claprve(request,id):
    r=ClinicReg.objects.get(id=id)
    r.Status='approved'
    r.save()
    return HttpResponse("<script>alert('Approved');window.location='/approveclin';</script>")

def approvearticle(request):
    d=Article.objects.raw("SELECT doctorapp_article.*,doctorapp_doctorreg.DrName FROM doctorapp_article,doctorapp_doctorreg WHERE doctorapp_doctorreg.id=doctorapp_article.docid AND doctorapp_article.Status='pending'")
    context = {'k':d}
    template = loader.get_template("approvearticle.html")
    return HttpResponse(template.render(context, request))

def artaprve(request,id):
    r=Article.objects.get(id=id)
    r.Status='approved'
    r.save()
    return HttpResponse("<script>alert('Approved');window.location='/approvearticle';</script>")

def approveques(request):
    d=Question.objects.raw("SELECT patientapp_question.*,patientapp_patientreg.Name FROM patientapp_question,patientapp_patientreg WHERE patientapp_patientreg.id=patientapp_question.pid and patientapp_question.Status='pending'")
    context = {'k':d}
    template = loader.get_template("approveques.html")
    return HttpResponse(template.render(context, request))

def quesaprve(request,id):
    r=Question.objects.get(id=id)
    r.Status='approved'
    r.save()
    return HttpResponse("<script>alert('Approved');window.location='/approveques';</script>")

def viewsugg(request):
    d=Question.objects.raw("SELECT patientapp_suggestion.*,patientapp_patientreg.Name FROM patientapp_suggestion,patientapp_patientreg WHERE patientapp_patientreg.id=patientapp_suggestion.pid")
    context = {'k':d}
    template = loader.get_template("viewsuggestions.html")
    return HttpResponse(template.render(context, request))
def banking(request):
    context = {}
    template = loader.get_template("banking.html")
    return HttpResponse(template.render(context, request))
def addbank(request):
    if request.method == "POST":

        bname=request.POST.get("bname")
        logo=request.FILES["logo"]

        s1=Bank.objects.all()
        for i in s1:
            if(i.bname == bname):
                return HttpResponse("<script>alert('already exist');window.location='/addbank';</script>")
        else:
            s=Bank()
            s.bname=bname
            s.logo=logo
            s.save()
            return HttpResponse("<script>alert('bank name added successfully');window.location='/addbank';</script>")
    else:
        context = {}
        template = loader.get_template("AddBank.html")
        return HttpResponse(template.render(context, request))
def addaccount(request):
    if request.method == "POST":
        bname = request.POST.get("drpbank")
        bankid = Bank.objects.get(id=bname)
        brname = request.POST.get("drpbranch")
        branchid = Branch.objects.get(id=brname)
        cname = request.POST.get("cname")
        cno = request.POST.get("cno")
        cvv = request.POST.get("cvv")
        year = request.POST.get("year")
        month = request.POST.get("month")
        amount = request.POST.get("amount")
        s = Account()

        s.cname = cname
        s.cno = cno
        s.cvv = cvv
        s.amount = amount
        s.year = year
        s.month = month
        s.bname = bankid.id
        s.branch = branchid.id
        s.save()
        return HttpResponse("<script>alert('account added successfully');window.location='/addaccount';</script>")
    else:
        b = Bank.objects.all()
        template = loader.get_template("AddAccount.html")
        context = {'bank': b}
        return HttpResponse(template.render(context, request))
def brnch(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        did = request.GET.get('q')
        l = Branch.objects.filter(bname=did).values()
        return JsonResponse(list(l), safe=False)


def addbranch(request):
    if request.method=="POST":
        bn=request.POST.get("drpbname")
        bid=Bank.objects.get(id=bn)
        brname=request.POST.get("branch")
        addr = request.POST.get("addr")
        ifsc = request.POST.get("ifsc")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        s=Branch()
        s.branch=brname
        s.address=addr
        s.email=email
        s.phone=phno
        s.ifsc=ifsc
        s.bname=bid.id
        s.save()
        return HttpResponse("<script>alert('branch added successfully');window.location='/addbranch';</script>")
    else:
        s = Bank.objects.all()
        template = loader.get_template("AddBranch.html")
        context = {'bank': s}
        return HttpResponse(template.render(context, request))