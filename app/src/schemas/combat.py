from schematics.models import Model
from schematics.types import ListType, StringType, ModelType


class PlayerSchema(Model):
    movimientos = ListType(StringType(), required=True)
    golpes = ListType(StringType(), required=True)


class CombatSchema(Model):
    player1 = ModelType(PlayerSchema, required=True)
    player2 = ModelType(PlayerSchema, required=True)
