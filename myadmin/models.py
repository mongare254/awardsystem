from django.db import models

# Create your models here.
class asession(models.Model):
    ses_name=models.CharField(max_length=1000)
    ses_start=models.DateTimeField()
    ses_stop=models.DateTimeField()
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.ses_name

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = asession.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except asession.DoesNotExist:
                pass
        super(asession, self).save(*args, **kwargs)
