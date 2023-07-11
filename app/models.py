from django.db import models
class Studentform(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sage=models.IntegerField()
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.sname

