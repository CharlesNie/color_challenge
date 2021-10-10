"""Color swatch related models
"""
from random import randint
from django.db import models


class Color(models.Model):
    """Color model with range of color value for generating a color dynamically

    Attributes:
        name (str): color name
        min_value (int): the minimum integer of a color value range
        max_value (int): the maximum integer of a color value range
    """

    name = models.CharField(max_length=100)
    min_value = models.IntegerField()
    max_value = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def random_value(self):
        """Randomly generate a color value within the range min_value to max_value"""
        if getattr(self, '_random_value', None) is None:
            self._random_value = randint(self.min_value, self.max_value)
        return self._random_value


class ColorSpace(models.Model):
    """ColorSpace model represents the composition of color space

    Attributes:
        name (str): color space name
        colors (many to many relationship to Color): colors included in color space
    """

    name = models.CharField(max_length=100)
    colors = models.ManyToManyField(Color, related_name="color_spaces")

    def __str__(self):
        return self.name
