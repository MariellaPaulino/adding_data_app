from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
 

# Create your views here.

def about(request):
    first_name = "Mariella" 
    last_name = "Paulino" 
    the_message = "Hello! My name is "+first_name+" "+last_name+" "+"and I am looking for an awesome software development position!!!"
    return HttpResponse (the_message)
    #PART 5: This is where all the information gets stored.  In other words, this is where all the information gets stored in a way that all the data gets translated in a language that HTML can use.  


def index (request):
    the_second_message = "INDEX is all obsessed about his windows. He carries Windex everywhere, what a weird dude!"
    return HttpResponse (the_second_message)