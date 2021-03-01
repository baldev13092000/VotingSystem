from django.conf.urls import url
from appTwo import views
app_name = 'appTwo'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^validation1/$',views.validation1,name = 'validation1'),
    url(r'^$',views.validation2,name = 'validation2'),
    url(r'^validation3/$',views.validation3,name = 'validation3'),
    url(r'^validation4/$',views.validation4,name = 'validation4'),
    url(r'^validation5/$',views.validation5,name = 'validation5'),
    url(r'^validation6/$',views.validation6,name = 'validation6'),
    url(r'^validation7/$',views.validation7,name = 'validation7'),
    url(r'^validation8/$',views.validation8,name = 'validation8'),
    url(r'^validation9/$',views.validation9,name = 'validation9'),
    url(r'^statistics/$',views.statistics,name='statistics'),
    url(r'^signup_next1/$',views.signup_next1,name='signup_next1'),
    url(r'^validation10/$',views.validation10,name = 'validation10'),
    url(r'^validation11/$',views.validation11,name = 'validation11'),
    url(r'^validation12/$',views.validation12,name = 'validation12'),
    url(r'^NewSmartCard/$',views.NewSmartCard,name = 'NewSmartCard'),
]
