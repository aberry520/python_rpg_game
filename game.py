class Fighter:
  def __init__(self, name, type, power = 10, health = 100):
    self.name = name
    self.type = type
    self.power = power
    self.health = health
    
  def stats(self):
    print(f"""Name: {self.name}
Type: {self.type}
Power: {self.power}
Health: {self.health}
""")
    
  def alive(self):
    if self.health <= 0:
      print(f"{self.name} died")
      return False
    else:
      return True
      
class Hero(Fighter):
  def attack(self, other_person):
    other_person.health -= self.power
    print(f"You do {self.power} damage to the goblin.")
    print(f"Goblins health is now {other_person.health}")
    

class Goblin(Fighter):
  def attack(self, other_person):
    other_person.health -= self.power
    print(f"Goblin attacks you and does {self.power} damage to you.")
    print(f"Your health is now at {other_person.health}")
    if self.health <= 0:
      print("The goblin is dead.")
###########################################
goblin = Goblin("Goblin", "Ghoul")
hero = Hero("Hero", "Hero")
###########################################


while goblin.alive() and hero.alive():
  hero.stats()
  goblin.stats()
  goblin.attack(hero)
  break

