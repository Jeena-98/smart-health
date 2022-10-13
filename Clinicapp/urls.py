from django.urls import path
import Clinicapp.views

urlpatterns = [
    path('clinichome/',Clinicapp.views.clinichome,name="clinichome"),
    path('clinictemp/', Clinicapp.views.clinictemp, name="clinictemp"),
    path('clinicreg/', Clinicapp.views.reg,name="clinicreg"),
    path('drop1/', Clinicapp.views.drop1, name="drop1"),
    path('drreg/', Clinicapp.views.drreg, name="drreg"),
    path('clinicdet/', Clinicapp.views.clinicdet, name="clinicdet"),
    path('det1/', Clinicapp.views.det1, name="det1"),
    path('det2/', Clinicapp.views.det2, name="det2"),


]
