from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
    #"Hi, you are in the second floor of the big building, which office would you like to go into?

    #PART 2: we have arived here from the big prent folder (adding_data_app/urls) and the line that said: url(r'^app/', include('app.urls').  
    #in this line, our app is telling you, you have differnt things that you can do when you have arrived in this step.  In this instance, our choices are about.  

    #our code is telling us, "oh, you want to go to about, please go to the vies.py file and follow the file that is called about."  
)