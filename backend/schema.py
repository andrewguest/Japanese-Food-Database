from api import ma
import models


class CandySchema(ma.ModelSchema):
    class Meta:
        model = models.Candy
