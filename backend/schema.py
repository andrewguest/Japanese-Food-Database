from extensions import ma
import models


class FoodSchema(ma.ModelSchema):
    class Meta:
        model = models.Food


class DrinkSchema(ma.ModelSchema):
    class Meta:
        model = models.Drink
