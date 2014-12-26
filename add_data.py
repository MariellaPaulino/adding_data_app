import csv #to get the python's csv tools 
from app.models import Women_Warriors
#STEP 10.1 I have just copied and edited the code

#the code below is copied from my instructor Aliya's "Code That Only Does One Thing" github page where she outlined the code to pull from a csv into an app for the an application. 
with open('warriors.csv', 'rb') as csvfile:
    warrior_list = csv.reader(csvfile, delimiter=',', quotechar='"')
    #and here you add the users
    for column in warrior_list:
        #In your CSV file you have certain objects that are within the different categories.  Lets look at the CSV in the first line... "Ellen Ochoa...    First Hispanic American woman astronaut...TRUE...    Mexican-American"... The categories for this are NAME...BIO...TRUE_LIFE...NATIONALITY... 

        #we are going to set up the line below based on this model... remember it starts on 0.. so for example the name Ane.. A=0, N=1, E=2
        w = Women_Warriors(name =column[0], nationality=column[1],  real_life=column[2],bio=column[3])
        w.save()

        #SUPER IMPORTANT = know the difference between row and column!!

#STEP 10.2 You may get an error that says, "django module settings are not configured... you will type in there: 
# $export DJANGO_SETTINGS_MODULE=adding_data_app.settings

#After you have set this up you will type to adding_data../adding_data$ python add_data.py from your terminal and run 