from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
 

# Create your views here.

def about(request):
#remember, the function 'def' is like the secretary that asks you, "hi, welcome, who are you here to see?  In this case, our function is ABOUT... and we are going to tell you what about is going to do below... REMEMBER, indents are important!"

    the_message = "Hello. I am all ABOUT that life"
    #PART 4.2: You are now defining the function about to tell you something, this is similar to what we did previously, but this time, because we have multiple functions, the way it will be written down will be a tad different. 

    return HttpResponse (the_message)

    #PART 3: In this part you have moved all the way into the building, up the stairs into the floor, into the office, and you are now wanting to speak and chat with someone very specific.  You want to speak to someone called Hello, and this is what you will see when you open the browser, a page that says hello" 

    #--> test the page by going to your server and typing... 8000/app/about/... your page should just be a page that says 'hello' -TEST PASS move on! 
    
    '''return HttpResponse ("hello")'''
    #PART 4.1: DELETE... you are no longer using this because you are moving on a multiple "people" within the page  

def index (request):
    #PART 4.3 we are bringing a new function to the page, or a new "person"  In this case, our new person is going to be Index.  We want the secretary to guide us to index
    the_second_message = "INDEX is all obsessed about his windows. He carries everywhere, what a weird dude!"
    return HttpResponse (the_second_message)