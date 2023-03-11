from schematics.models import Model
from schematics.types import ListType, StringType, ModelType


class PlayerSchema(Model):
    movimientos = ListType(StringType(max_length=5), required=True)
    golpes = ListType(StringType(max_length=1), required=True)


class CombatSchema(Model):
    player1 = ModelType(PlayerSchema, required=True)
    player2 = ModelType(PlayerSchema, required=True)
