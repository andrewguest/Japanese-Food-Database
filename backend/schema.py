import models
from api import ma


class FoodSchema(ma.ModelSchema):
    class Meta:
        model = models.Food


class DrinkSchema(ma.ModelSchema):
    class Meta:
        model = models.Drink
