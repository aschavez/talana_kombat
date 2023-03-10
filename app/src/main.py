import falcon
import json
from schematics.exceptions import DataError

from middlewares.require_json import RequireJSON
from middlewares.body_parser import BodyParser

import config
from schemas.combat import CombatSchema
from models.player import PlayerModel
from controllers.combat import CombatController


class CombatResource:
    def on_post(self, req, resp):
        try:
            combat_data = CombatSchema(req.context['body'])
            combat_data.validate()

            player01 = PlayerModel(**config.data_players['player01'])
            player02 = PlayerModel(**config.data_players['player02'])
            combat = CombatController(player01, player02)
            combat.set_commands(combat_data['player1'], combat_data['player2'])
        except (DataError) as e:
            raise falcon.HTTPBadRequest(description=json.loads(str(e)))


api = falcon.App(
    middleware=[
        RequireJSON(),
        BodyParser(),
    ]
)
combat = CombatResource()

api.add_route('/combat', combat)
