from django.db import models

# Create your models here.

class Users(models.Model):
    device_id = models.CharField(max_length=200)
    visits = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.device_id
