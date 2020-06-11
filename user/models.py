from django.db import models

# Create your models here
class Award(models.Model):
    award_name=models.CharField(max_length=100)
    award_description =models.TextField()

    def __str__(self):
        return self.award_name

class Nominee(models.Model):
    award=models.CharField(max_length=300)
    nominee_name=models.CharField(max_length=50, null=True,default='Nominee')
    session= models.CharField(max_length=50, default='thissession')
    reason=models.TextField(max_length=1000)
    impact =models.TextField(max_length=1000)
    username=models.CharField(max_length=200, null=True,default='CurrentUser')

    def __str__(self):
        str_name=str(self.nominee_name)
        str_award =str(self.award)
        return str_name +" "+str_award