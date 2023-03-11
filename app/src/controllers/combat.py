from models.player import PlayerModel
from exceptions import CombatException, DeadException


class CombatController:

    def __init__(self, players: list[PlayerModel]) -> None:
        if len(players) != 2: raise CombatException('Son necesarios 2 jugadores para el combate.')
        self.player01 = players[0]
        self.player02 = players[1]

    def set_commands(self, p1_cmds: dict, p2_cmds: dict) -> None:
        self.player01.commands = p1_cmds
        self.player01.turn_commands = [f"{m}+{g}" for m, g in zip(
            p1_cmds['movimientos'], p1_cmds['golpes']
        )]
        self.player02.commands = p2_cmds
        self.player02.turn_commands = [f"{m}+{g}" for m, g in zip(
            p2_cmds['movimientos'], p2_cmds['golpes']
        )]

    def define_turns(self) -> tuple[PlayerModel, PlayerModel]:
        if len(self.player01.turn_commands) < len(self.player02.turn_commands):
            return self.player01, self.player02
        elif len(self.player01.turn_commands) > len(self.player02.turn_commands):
            return self.player02, self.player01
        elif len(self.player01.commands['movimientos']) < len(self.player02.commands['movimientos']):
            return self.player01, self.player02
        elif len(self.player01.commands['movimientos']) > len(self.player02.commands['movimientos']):
            return self.player02, self.player01
        elif len(self.player01.commands['golpes']) < len(self.player02.commands['golpes']):
            return self.player01, self.player02
        elif len(self.player01.commands['golpes']) > len(self.player02.commands['golpes']):
            return self.player02, self.player01
        else:
            return self.player01, self.player02

    def play(self) -> list[str]:
        turns_description = []
        first_player, second_player = self.define_turns()
        try:
            for turn in range(max(len(first_player.turn_commands), len(second_player.turn_commands))):
                turn_desc, damage_points = first_player.execute_command(turn)
                turns_description.append(turn_desc)
                second_player.receive_damage(damage_points)

                turn_desc, damage_points = second_player.execute_command(turn)
                turns_description.append(turn_desc)
                first_player.receive_damage(damage_points)
        except DeadException as e:
            if first_player.is_dead() and not second_player.is_dead():
                turns_description.append(f"{second_player.name} gana la pelea y aún le queda {second_player.energy_points} de energía")
        return turns_description
