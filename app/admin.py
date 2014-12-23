from django.contrib import admin
from models import Women_Warriors
#PART 6.4 see the line above, don't forget to tell the page from where it is supposed to pull!! I forgot about this line and was getting into hella errors. Super important. 

admin.site.register(Women_Warriors)
#PART 6.5 You are telling the admin site, 'hey, little app here, you are going to refer to the modles I have set up for this specific app from the models called Powerful_Warriors"  Remember, you are doing this from the 
