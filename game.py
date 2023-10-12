
class Fighter:
    def __init__(self, name = "", type = "", power = 10, health = 100):
      self.name = name
      self.type = type
      self.power = power
      self.health = health

    def attack(self, other_person):
      print(f'{self.name} attacks {other_person.name}!')
    
    def stats(self):
      print(f"""Name: {self.name}
Type: {self.type}
Power: {self.power}
Health: {self.health}
""")
###########################################
goblin = Fighter()
hero = Fighter()