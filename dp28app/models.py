from django.db import models

# Create your models here.
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.


class Topic(models.Model):
    topic_name=models.CharField(max_length=100,unique=True,blank=False,validators=[validators.MaxLengthValidator(10)])

    def __str__(self):
        return self.topic_name

def validatename(name):
    if not name.isalpha():
        raise ValidationError("{} is having characters other than alphabets".format(name))
    
class WebPage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False,validators=[validatename])
    url=models.URLField(max_length=100,blank=False,unique=True)

    def __str__(self):
        return self.name

class AccessDetails(models.Model):
    webpage=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    datetime=models.DateTimeField()

    def dt(datetime):
        return datetime