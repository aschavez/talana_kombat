from models.player import PlayerModel


class CombatController:

    def __init__(self, player01: PlayerModel, player02: PlayerModel) -> None:
        self.player01 = player01
        self.player02 = player02

    def set_commands(self, p1_cmds: dict, p2_cmds: dict) -> None:
        self.player01.commands = [f"{m}+{g}" for m, g in zip(
            p1_cmds['movimientos'], p1_cmds['golpes']
        )]
        self.player02.commands = [f"{m}+{g}" for m, g in zip(
            p2_cmds['movimientos'], p2_cmds['golpes']
        )]

    def define_turns(self):
        return

    def play(self) -> str:
        first, second = self.define_turns()
