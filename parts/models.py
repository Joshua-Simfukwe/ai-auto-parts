from django.db import models

class CarShape(models.Model):
    """
    Basic model to represent the general shape of a vehicle
    (sedan, hatchback, SUV, truck, etc.)
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Car Shape"
        verbose_name_plural = "Car Shapes"

    def __str__(self):
        return self.name
