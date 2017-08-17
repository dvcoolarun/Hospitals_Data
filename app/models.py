from django.db import models

class bloodbankdata(models.Model):
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Hospital_name = models.TextField()
    Contact = models.TextField()
    Address = models.TextField()
