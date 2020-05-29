from django.conf.urls import url
from . import views

app_name = 'mid_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^doctors/$', views.doctors, name='doctors'),
    url(r'^about/$', views.about, name='about'),
    url(r'^duasreminders/$', views.duasreminders, name='duasreminders'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^share_stories/$', views.share_stories, name='share_stories'),
    url(r'^funactivities/$', views.funactivities, name='funactivities'),
    url(r'^connect/$', views.connect, name='connect'),
    # url(r'^choice/$', views.choice, name='choice'),
    # url(r'^doctor-signup/$', views.DoctorSignup.as_view(), name='DoctorSignup'),
    
]