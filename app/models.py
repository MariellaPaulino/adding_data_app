from django.db import models

# PART 6.1: You have to edit your models and your settings. The difference between the two is this.  Things of your SETTINGS as the PARENT project.  When you do a project with multiple apps, they are all pulling from the same database.  Think of Google.  Google has ONE HUGE (super creepy) database.  All the apps pull drom that similar database.  Each app, however, runs on a different set of data (the models that we will edit in here), and so we have to pull from that big data in the big database (in the settings!)  
    
class Women_Warriors(models.Model):
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    real_life = models.BooleanField(default=True)
    bio = models.TextField()