from django.urls import path
import Adminapp.views

urlpatterns = [
    path('', Adminapp.views.index,name="index"),
    path('login/', Adminapp.views.login, name='login'),
    path('Admin/',Adminapp.views.adminhome,name='adminhome'),
    path('addstate/', Adminapp.views.addstate,name='addstate'),
    path('adddist/', Adminapp.views.adddist, name='adddist'),
    path('addplace/', Adminapp.views.addplace, name='addplace'),
    path('drop/', Adminapp.views.drop, name='drop'),
    path('specialization/', Adminapp.views.specialization, name='specialization'),
    path('approvedr/', Adminapp.views.approvedr, name='approvedr'),
    path('draprve/<id>', Adminapp.views.draprve, name='draprve'),
    path('approveclin/', Adminapp.views.approveclin, name='approveclin'),
    path('claprve/<id>', Adminapp.views.claprve, name='claprve'),
    path('approvearticle/', Adminapp.views.approvearticle, name='approvearticle'),
    path('artaprve/<id>', Adminapp.views.artaprve, name='artaprve'),
    path('approveques/', Adminapp.views.approveques, name='approveques'),
    path('quesaprve/<id>', Adminapp.views.quesaprve, name='quesaprve'),
    path('viewsugg/', Adminapp.views.viewsugg, name='viewsugg'),
    path('banking/', Adminapp.views.banking, name='banking'),
    path('addbank/', Adminapp.views.addbank, name='bank'),
    path('addbranch/', Adminapp.views.addbranch, name='branch'),
    path('addaccount/', Adminapp.views.addaccount, name='account'),
    path('brnch/', Adminapp.views.brnch, name='brnch'),

]