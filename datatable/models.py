from django.db import models

# Create your models here.
class Userback(models.Model):
    teltype = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    questiontype = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'userback'


