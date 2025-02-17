from django.db import models


# Create your models here.
class location(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

# creating leaderimage model
class yo(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    def __str__(self):
        return self.title

class Imageleader(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    description1 = models.TextField(max_length=1000,default='')
    manifesto1=models.CharField(max_length=200,default='')
    manifesto2=models.CharField(max_length=200,default='')
    manifesto3=models.CharField(max_length=200,default='')
    party=models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='image')
    cat = models.ForeignKey(location, on_delete=models.CASCADE)
    def __str__(self):
        return self.title