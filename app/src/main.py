import falcon
import json
from schematics.exceptions import DataError

from middlewares.require_json import RequireJSON
from middlewares.body_parser import BodyParser

import config
from schemas.combat import CombatSchema
from models.player import PlayerModel
from controllers.combat import CombatController
from exceptions import CombatException


class CombatResource:
    def on_post(self, req, resp):
        try:
            combat_data = CombatSchema(req.context['body'])
            combat_data.validate()

            player_tonyn = PlayerModel(
                **config.data_players['tonyn_stallone'])
            player_arnaldor = PlayerModel(
                **config.data_players['arnaldor_shuatseneguer'])

            combat = CombatController([player_tonyn, player_arnaldor])
            combat.set_commands(combat_data['player1'], combat_data['player2'])
            turns_description = combat.play()
            resp.body = json.dumps({
                'winner': str(player_tonyn) if not player_tonyn.is_dead() else str(player_arnaldor),
                'turns_desc': turns_description,
            })
        except DataError as e:
            raise falcon.HTTPBadRequest(description=json.loads(str(e)))
        except CombatException as e:
            raise falcon.HTTPBadRequest(description=str(e))


api = falcon.App(
    middleware=[
        RequireJSON(),
        BodyParser(),
    ]
)
combat = CombatResource()

api.add_route('/combat', combat)
