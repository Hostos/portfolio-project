from django.db import models

#essentially defines the Blog object with initial states/characteristics
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    #displasy the actual blog title when listed in django
    def __str__(self):
        return (self.title)

    #these are the methods of the object defined in this model
    def summary(self):
        #returns the first 100 characters of the body
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')



