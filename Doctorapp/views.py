from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import Article,Prescription,Doctorreg,Medihis
from Patientapp.models import Patientreg,Appointment,Question
from django.http import JsonResponse

# Create your views here.
def doctorhome(request):
    context={}
    template=loader.get_template("doctorhome.html")
    return HttpResponse(template.render(context,request))

def doctortemp(request):
    context={}
    template=loader.get_template("doctortemp.html")
    return HttpResponse(template.render(context,request))

def medihis(request):
    if request.method=='POST':
        m=Medihis()
        pname=request.POST.get("pname")
        bgroup = request.POST.get("bgroup")
        ht = request.POST.get("ht")
        wt = request.POST.get("wt")
        phy = request.POST.get("phy")
        smoke = request.POST.get("smoke")
        drinking = request.POST.get("drinking")
        disease = request.POST.get("disease")
        reaction = request.POST.get("reaction")
        med = request.POST.get("med")
        dos = request.POST.get("dos")
        pur = request.POST.get("pur")
        diab = request.POST.get("diab")
        sugar = request.POST.get("sugar")
        allergy = request.POST.get("allergy")
        famhis = request.POST.get("famhis")
        immunity = request.POST.get("immunity")
        tb = request.POST.get("tb")
        chest = request.POST.get("chest")
        stroke = request.POST.get("stroke")
        rhm = request.POST.get("rhm")
        attack = request.POST.get("attack")
        mvp = request.POST.get("mvp")
        asthma = request.POST.get("asthma")
        pace = request.POST.get("pace")
        thyroid = request.POST.get("thyroid")
        uname = request.session["uname"]
        d = Doctorreg.objects.get(Uname=uname)
        m.pid=pname
        m.docid=d.id
        m.Bgroup=bgroup
        m.Height=ht
        m.Weight=wt
        m.Physician=phy
        m.Smoke=smoke
        m.Drink=drinking
        m.Disease=disease
        m.Reaction=reaction
        m.Medicine=med
        m.Dosage=dos
        m.Purpose=pur
        m.Diabetic=diab
        m.Sugar=sugar
        m.Allergy=allergy
        m.Family=famhis
        m.Immunity=immunity
        m.Tb=tb
        m.Chest=chest
        m.Stroke=stroke
        m.Fever=rhm
        m.Attack=attack
        m.MVP=mvp
        m.Asthma=asthma
        m.Pacemaker=pace
        m.Thyroid=thyroid
        m.save()
        return HttpResponse("<script>alert('Medical History Added Successfully');window.location='/medihis';</script>")
    else:
        uname = request.session["uname"]
        d = Doctorreg.objects.get(Uname=uname)
        p = Appointment.objects.raw("SELECT patientapp_patientreg.Name,patientapp_patientreg.id,patientapp_appointment.pid FROM patientapp_patientreg  INNER JOIN patientapp_appointment on patientapp_patientreg.id=patientapp_appointment.pid INNER JOIN doctorapp_doctorreg ON doctorapp_doctorreg.id=patientapp_appointment.docid WHERE doctorapp_doctorreg.id='%s'",[d.id])
        context = {'k': p}
        template=loader.get_template("medicalhistory.html")
        return HttpResponse(template.render(context,request))

def prescribe(request):
    if request.method=='POST':
        p=Prescription()
        pname=request.POST.get("pname")
        medi=request.POST.get("medicine")
        dosage=request.POST.get("dosage")
        nod=request.POST.get("nod")
        uname = request.session["uname"]
        d = Doctorreg.objects.get(Uname=uname)
        p.pid=pname
        p.docid=d.id
        p.Medicine=medi
        p.Dosage=dosage
        p.Nod=nod
        p.save()
        return HttpResponse("<script>alert('Prescription Added Successfully');window.location='/prescribe';</script>")
    else:
        uname = request.session["uname"]
        d = Doctorreg.objects.get(Uname=uname)
        p = Appointment.objects.raw("SELECT patientapp_patientreg.Name,patientapp_patientreg.id, patientapp_appointment.pid FROM patientapp_patientreg  INNER JOIN patientapp_appointment on patientapp_patientreg.id=patientapp_appointment.pid INNER JOIN doctorapp_doctorreg ON doctorapp_doctorreg.id=patientapp_appointment.docid WHERE doctorapp_doctorreg.id='%s'",[d.id])
        context={'k':p}
        template=loader.get_template("prescribemedicines.html")
        return HttpResponse(template.render(context,request))

def article(request):
    if request.method=='POST':
        a=Article()
        title=request.POST.get("title")
        file=request.FILES['file']
        uname = request.session["uname"]
        d = Doctorreg.objects.get(Uname=uname)
        a.docid=d.id
        a.Title=title
        a.File=file
        a.Status='pending'
        a.save()
        return HttpResponse("<script>alert('Article Added Successfully');window.location='/article';</script>")
    else:
        context={}
        template=loader.get_template("articleupload.html")
        return HttpResponse(template.render(context,request))

def viewques(request):
    q=Question.objects.raw("SELECT patientapp_patientreg.Name,patientapp_question.* FROM patientapp_question,patientapp_patientreg WHERE patientapp_patientreg.id=patientapp_question.pid and patientapp_question.Status='approved' AND patientapp_question.Ans=''")
    context = {'k':q}
    template = loader.get_template("viewques.html")
    return HttpResponse(template.render(context, request))

def reply(request,id):
    if request.method=='POST':
        q=Question.objects.get(id=id)
        ans=request.POST.get("ans")
        q.Ans=ans
        q.save()
        return HttpResponse("<script>alert('Replied Successfully');window.location='/viewques';</script>")
    else:
        context={}
        template=loader.get_template("replyqueries.html")
        return HttpResponse(template.render(context,request))

def viewappdr(request):
    uname = request.session["uname"]
    d = Doctorreg.objects.get(Uname=uname)
    a=Appointment.objects.raw("SELECT patientapp_patientreg.Name,patientapp_appointment.* FROM patientapp_patientreg  INNER JOIN patientapp_appointment on patientapp_patientreg.id=patientapp_appointment.pid INNER JOIN doctorapp_doctorreg ON doctorapp_doctorreg.id=patientapp_appointment.docid WHERE doctorapp_doctorreg.id='%s'",[d.id])
    context = {'k':a}
    template = loader.get_template("dr_viewappoin.html")
    return HttpResponse(template.render(context, request))

def canceldr(request,id):
    a=Appointment.objects.get(id=id)
    a.delete()
    return HttpResponse("<script>alert('Appointment Cancelled');window.location='/viewappdr';</script>")