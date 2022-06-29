from django.db import models

# Create your models here.

class VolumeList(models.Model):
    volume = models.IntegerField()

    def __str__(self) -> str:
        return str(self.volume)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    volume = models.ForeignKey(
        VolumeList, 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name



