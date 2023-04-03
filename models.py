from django.db import models

# Create your models here.
#ORM -->object relational mapper

class Animal(models.Model):
    animal_name = models.CharField(max_length=20,null=True)
    animal_type = models.CharField(max_length=20,null=True)
    animal_sound = models.CharField(max_length=20,null=True)

