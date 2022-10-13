from django.urls import path
import Doctorapp.views

urlpatterns = [
    path('doctorhome/', Doctorapp.views.doctorhome, name="doctorhome"),
    path('doctortemp/', Doctorapp.views.doctortemp, name="doctortemp"),
    path('medihis/',Doctorapp.views.medihis,name="medihis"),
    path('prescribe/', Doctorapp.views.prescribe, name="prescribe"),
    path('article/', Doctorapp.views.article, name="article"),
    path('viewques/', Doctorapp.views.viewques, name="viewques"),
    path('reply/<id>', Doctorapp.views.reply, name="reply"),
    path('viewappdr/', Doctorapp.views.viewappdr, name="viewappdr"),
    path('canceldr/<id>', Doctorapp.views.canceldr, name="canceldr"),

]