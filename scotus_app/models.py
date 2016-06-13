from django.db import models


class SupremeCourtJustice(models.Model):
    name = models.CharField(max_length=50)
    law_school = models.CharField(max_length=50)
    speech = models.URLField()
    photo = models.URLField(null=True)
    hobby = models.CharField(max_length=50)
    gender = models.CharField(max_length=2)
    birth_date = models.DateField()
    appointed_by = models.CharField(max_length=20)

    def __str__(self):
        return self.name


