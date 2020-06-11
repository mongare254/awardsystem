from django.db import models

# Create your models here.
class winner(models.Model):
    winner_choices=(
        (1, 'FIRST'),
        (2, 'SECOND'),
        (3, 'THIRD'),
    )
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    dept =models.CharField(max_length=100)
    award=models.CharField(max_length=100)
    position=models.IntegerField(choices=winner_choices)

    def __str__(self):
        return self.first_name +" "+self.second_name +" " +self.award