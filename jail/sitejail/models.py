from django.db import models


class Prisoner(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    behaviour = models.TextField()
    date_of_conclusion = models.DateTimeField()
    image = models.ImageField(upload_to="image", null=True, default="C:/Users/asus/Downloads/default.png")
