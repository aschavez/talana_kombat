import random
import typing

import config
from exceptions import DeadException


class PlayerModel:

    def __init__(self, name: str, lastname: str, energy_points: int, direction: str, special_moves: dict, moves: dict) -> None:
        self.name = name
        self.lastname = lastname
        self.energy_points = energy_points
        self.direction = direction
        self.special_moves = special_moves
        self.moves = moves
        self.commands = {}
        self.turn_commands = []

    def is_dead(self) -> bool:
        return self.energy_points <= 0

    def is_special_move(self, turn_command: str) -> tuple[bool, list, typing.Union[str, None]]:
        for k, v in self.special_moves.items():
            if k in turn_command.upper():
                add_moves = turn_command[:-len(k)]
                return True, list(add_moves), v
        return False, [], None

    def is_normal_move(self, command: str) -> tuple[bool, typing.Union[str, None]]:
        if command.upper() in self.moves:
            return True, self.moves[command.upper()]
        else:
            return False, None

    def receive_damage(self, damage_points: int) -> None:
        new_energy = self.energy_points - damage_points
        self.energy_points = 0 if new_energy <= 0 else new_energy
        if self.energy_points == 0:
            raise DeadException(f"{self.name} is dead")

    def describe_moves(self, moves: list, is_only: bool = True) -> str:
        if len(moves) == 0: return ''

        list_moves_desc = [config.moves_desc[self.direction][m.upper()] for m in moves]
        if is_only:
            if len(list_moves_desc) == 1:
                return f" {list_moves_desc[0]}"
            else:
                return f" {', '.join(list_moves_desc[:-1])} y {list_moves_desc[-1]}"
        else:
            return f" {', '.join(list_moves_desc)} y"

    def execute_command(self, turn: int) -> tuple[str, int]:
        try:
            is_sm, add_moves, sm = self.is_special_move(self.turn_commands[turn])
            if is_sm:
                return f"{self.name}{self.describe_moves(add_moves, False)} {random.choice(config.special_words)} un {sm['name']}", sm['energy_points']

            is_nm, nm = self.is_normal_move(self.commands['golpes'][turn])
            if is_nm:
                return f"{self.name}{self.describe_moves(list(self.commands['movimientos'][turn]), False)} da {nm['name']}", nm['energy_points']

            if len(self.commands['movimientos'][turn]) > 0:
                return f"{self.name}{self.describe_moves(list(self.commands['movimientos'][turn]))}", 0

            return f"{self.name} no hace nada", 0
        except IndexError:
            return f"{self.name} no hace nada", 0

    def __repr__(self):
        return f"<{self.name} {self.lastname} | {self.energy_points} pts>"

    def __str__(self):
        return f"{self.name} {self.lastname}"
