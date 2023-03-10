class PlayerModel:

    def __init__(self, name: str, energy_points: int, moves: dict) -> None:
        self.name = name
        self.energy_points = energy_points
        self.moves = moves
        self.commands = []

    def is_alive(self) -> bool:
        return self.energy_points > 0

    def damage(self, energy_points: int) -> None:
        new_energy = self.energy_points - energy_points
        self.energy_points = 0 if new_energy <= 0 else new_energy
        if self.energy_points == 0:
            raise Exception(f"{self.name} is dead")

    def __repr__(self):
        return f"<{self.name} | {self.energy_points} pts>"
