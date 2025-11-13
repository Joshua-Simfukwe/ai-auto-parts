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
    
class PartCategory(models.Model):
    """
    Hierarchical category for organizing auto parts.
    Example:
        - Engine
        - Engine > Cooling
        - Engine > Cooling > Radiators
    """
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Part Category"
        verbose_name_plural = "Part Categories"
        unique_together = ('name', 'parent')

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name


class Part(models.Model):
    """"
    Base autp part model.
    Exmaple:
        name="Radiator"
        brand="Denso"
        category=Cooling > Radiators
    """
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(PartCategory, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Part"
        verbose_name_plural = "Parts"

    def __str__(self):
        return f"{self.brand} {self.name}".strip()