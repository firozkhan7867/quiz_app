from django.db import models
from datetime import datetime

# Create your models here.

class Participants(models.Model):
    f_name = models.CharField(max_length=300)
    l_name = models.CharField(max_length=300)
    email  = models.CharField(max_length=50)
    phone = models.IntegerField()
    score = models.IntegerField()
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.f_name