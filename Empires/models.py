from django.db import models

# Create your models here.


class AgeofEmpries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=100)
    description = models.TextField()
    expansion = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    created_in = models.DateTimeField(auto_now_add=True)
    build_time = models.DateTimeField(auto_now_add=True)
    reload_time = models.DateTimeField(auto_now_add=True)
    attack_delay = models.IntegerField()
    movement_rate = models.IntegerField()
    line_of_sight = models.IntegerField()
    hit_points = models.IntegerField()
    range = models.CharField(max_length=50)
    attack = models.IntegerField()
    armor = models.CharField(max_length=50)
    attack_bonus = models.CharField(max_length=50)
    armor_bonus = models.CharField(max_length=50)
    search_radius = models.IntegerField()
    accuracy = models.CharField(max_length=50)
    blast_radius = models.IntegerField()



    def __str__(self):
        return self.name
