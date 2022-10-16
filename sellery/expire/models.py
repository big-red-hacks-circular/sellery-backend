from django.db import models

class Expire(models.Model):
    category = models.CharField(max_length=200)
    fridge_lower = models.DurationField(null=True, blank=True)
    fridge_upper = models.DurationField(null=True, blank=True)
    freezer_lower = models.DurationField(null=True, blank=True)
    freezer_upper = models.DurationField(null=True, blank=True)
    pantry_lower = models.DurationField(null=True, blank=True)
    pantry_upper = models.DurationField(null=True, blank=True)
    default_pref = models.CharField(max_length=3, choices=[
        ('FRI', 'Fridge'),
        ('FRE', 'Freezer'),
        ('PAN', 'Pantry'),
    ], default='FRI')

    def __str__(self):
        return self.category