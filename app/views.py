from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def about(request):
    #'Hi you are in room number 123, who would you like to speak to?'

    #PART 3: In this part you have moved all the way into the building, up the stairs into the floor, into the office, and you are now wanting to speak and chat with someone very specific.  You want to speak to someone called Hello, and this is what you will see when you open the browser, a page that says hello"
    return HttpResponse ("hello")