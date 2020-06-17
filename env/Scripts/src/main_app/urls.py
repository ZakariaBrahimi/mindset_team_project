from django.conf.urls import url
from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^story/(?P<story_id>\d+)/(?P<story_slug>.+)/$', views.one_story, name='one_story'),
    url(r'^doctors/$', views.doctors, name='doctors'),
    url(r'^about/$', views.about, name='about'),
    url(r'^duasreminders/$', views.duasreminders, name='duasreminders'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^add-article/$', views.add_post, name='add_article'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^share_stories/$', views.share_stories, name='share_stories'),
    url(r'^add-story/$', views.add_story, name='add_story'),
    url(r'^funactivities/$', views.funactivities, name='funactivities'),
    # url(r'^one_post/(?P<slug>[-\w]+)/(?P<one_post_id>\d+)/$', views.one_post, name='one_post'),


    # url(r'^choice/$', views.choice, name='choice'),
    # url(r'^doctor-signup/$', views.DoctorSignup.as_view(), name='DoctorSignup'),
    
]