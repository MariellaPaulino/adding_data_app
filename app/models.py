from django.db import models

# PART 6.1: You have to edit your models and your settings. The difference between the two is this.  Things of your SETTINGS as the PARENT project.  When you do a project with multiple apps, they are all pulling from the same database.  Think of Google.  Google has ONE HUGE (super creepy) database.  All the apps pull drom that similar database.  Each app, however, runs on a different set of data (the models that we will edit in here), and so we have to pull from that big data in the big database (in the settings!)  
    
class Women_Warriors(models.Model):
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    real_life = models.BooleanField(default=True)
    bio = models.TextField()

    # PART 9: Objects exist in the mind of a computer.  "Computer language".  The computer doesn't understand that human lnaguage is useful.  Because it is not useful to it.  The computer understands 0s and 1s.  'Unicode' is the map that computer scientist developed to translate computer language to human text.  WHen you go on the admin site, before you put the line below, the site would list, the data you have put on the site as "Women_Warriors object"  After you have put this line in the site, the site lists these women by their name, since this is what you are telling the site to translate it to. 
    def __unicode__(self):
        return self.name