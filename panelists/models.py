from django.db import models
# Create your models here.
class winner(models.Model):
    winner_choices=(
        (1, 'FIRST'),
        (2, 'SECOND'),
        (3, 'THIRD'),
    )
    winner_name=models.CharField(max_length=100)
    dept =models.CharField(max_length=100)
    award=models.CharField(max_length=100)
    position=models.IntegerField(choices=winner_choices)
    description=models.TextField(default="I didnt know")



    def __str__(self):
        return self.first_name +" "+self.second_name +" " +self.award

class Panelist(models.Model):
    username=models.CharField(max_length=50)
    session=models.CharField(max_length=50)
    for_year=models.CharField(default='2020', max_length=50)

    def __str__(self):
        return self.username


