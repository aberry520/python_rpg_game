class Fighter:
    def __init__(self, name, power, health):
      self.name = name
      self.power = power
      self.health = health

    def attack(self, other_person):
      print(f'{self.name} attacks {other_person.name}!')

