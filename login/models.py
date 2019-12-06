from django.db import models

class User(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=64, blank=True, null=True)
    blog = models.CharField(max_length=64, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    maincolor = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'user'
