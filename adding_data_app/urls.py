from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover

urlpatterns = patterns('',
    #"Hi you are in the big building, where do you want to go?

    #this is basically saying, hi, you are in building the main buildng, here are the different places you can go, in this case, we have the option of going to the app folder, or basically going on the Maps app within Google. REMEMBER: Django has projects, and inside these projects are apps.  If we create multiple apps here they are going to be like Maps, Gmail, Calendar... etc... all drawing from the parent app.'''
    url(r'^app/', include('app.urls')),
    #PART 1: in the line above you are saying, yo, I want to you to go to the apps folder and open the urls.py file... part 1 
    url(r'^admin/', include(admin.site.urls)),
)