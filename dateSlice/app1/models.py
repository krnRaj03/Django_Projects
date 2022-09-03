from django.db import models

# Create your models here.

class test(models.Model):
  name=models.CharField(max_length=50,null=True)
  startdate=models.DateField(null=True)
  enddate=models.DateField(null=True)
  
  def __self__(self):
    return self.name