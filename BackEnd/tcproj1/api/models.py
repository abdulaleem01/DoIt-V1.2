from enum import unique
from django.db import models

# Create your models here.

class TcData(models.Model):
    tcnum = models.CharField(max_length = 7,unique = True )
    tcname = models.CharField(max_length = 200)
    tcdata = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
