from django.urls import path
import Patientapp.views

urlpatterns = [
    path('patienthome/', Patientapp.views.patienthome, name="patienthome"),
    path('patientreg/',Patientapp.views.patientreg,name="patientreg"),
    path('appointment/', Patientapp.views.appointment, name="appointment"),
    path('patienttemp/', Patientapp.views.patienttemp, name="patienttemp"),
    path('drop3/', Patientapp.views.drop3, name="drop3"),
    path('drop4/', Patientapp.views.drop4, name="drop4"),
    path('queries/', Patientapp.views.queries, name="queries"),
    path('sugg/', Patientapp.views.suggestion, name="sugg"),
    path('app1/', Patientapp.views.app1, name="app1"),
    path('app2/', Patientapp.views.app2, name="app2"),
    path('viewapp/', Patientapp.views.viewapp, name="viewapp"),
    path('cancel/<id>', Patientapp.views.cancel, name="cancel"),
    path('viewans/', Patientapp.views.viewans, name="viewans"),
    path('viewmed/', Patientapp.views.viewmed, name="viewmed"),
    path('search/', Patientapp.views.search, name="search"),
    path('drp/', Patientapp.views.drp, name="drp"),
    path('drp3/', Patientapp.views.drp3, name='drp3'),
    path('payment/', Patientapp.views.payment1, name='payment'),
    path('paymentcon/', Patientapp.views.paymentcon, name='paymentcon'),
    path('savepayment/', Patientapp.views.savepayment, name='savepayment'),
    path('viewpre/', Patientapp.views.viewpre, name="viewpre"),

]