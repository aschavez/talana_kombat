import re
from schematics.models import Model
from schematics.types import ListType, StringType, ModelType
from schematics.exceptions import ValidationError


class MoveType(StringType):
    def validate_move(self, value):
        if re.compile(r'[^WASDwasd]').search(value):
            raise ValidationError('Los movimientos solo pueden ser W, A, S o D')


class KickType(StringType):
    def validate_kick(self, value):
        if value not in ['P', 'K', 'p', 'k', '']:
            raise ValidationError('El golpe solo puede ser P o K')


class PlayerSchema(Model):
    movimientos = ListType(MoveType(max_length=5), required=True)
    golpes = ListType(KickType(max_length=1), required=True)


class CombatSchema(Model):
    player1 = ModelType(PlayerSchema, required=True)
    player2 = ModelType(PlayerSchema, required=True)
