class Character:
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
      
class Hero(Character):
  def attack(self, other_person):
    other_person.health -= self.power
    print(f"\nYou do {self.power} damage to the goblin.")
    print(f"Goblins health is now {other_person.health}\n")
    

class Goblin(Character):
  def attack(self, other_person):
    other_person.health -= self.power
    print(f"\nGoblin attacks you and does {self.power} damage to you.")
    print(f"Your health is now at {other_person.health}\n")
###########################################
goblin = Goblin("Goblin", "Ghoul")
hero = Hero("Hero", "Hero")
###########################################

def intro():
  hero.name = input("What is your name hero?\n")
  print("\nWhat kind of warrior are you?")
  print("1) Heavy Hitter")
  print("2) Great Health")
  print("3) Solid Warrior\n")
  hero_type = input("Choose 1, 2, or 3: ")
  try:
    hero_type = int(hero_type)
  except ValueError:
    hero_type = 3
    print("\nINVALID CHOICE you get Solid Warrior")

  if hero_type == 1:
    hero.power = 25
    hero.health = 50
    hero.type = "Heavy Hitter"
    hero.stats()
  elif hero_type == 2:
    hero.power = 10
    hero.health = 100
    hero.type = "Great Health"
    hero.stats()
  elif hero_type == 3:
    hero.power = 15
    hero.health = 80
    hero.type = "Solid Warrior"
    hero.stats()
  elif hero_type > 3 or hero_type < 1:
    print("\n INVALID CHOICE you get Solid Warrior")    
    hero.power = 15
    hero.health = 80
    hero.type = "Solid Warrior"
    hero.stats()
  

#######GAME_PLAY############
intro()
while goblin.alive() and hero.alive():
  print("What do you want to do?")
  print("1. fight goblin")
  print("2. do nothing")
  print("3. flee")
  user_input = input("Choose 1, 2, or 3: ")
  try:
    user_input = int(user_input)
  except ValueError:
    user_input = 50
    # print("INVALID CHOICE\n")
  
  if user_input == 1:
    hero.attack(goblin)
    if goblin.health > 0:
      goblin.attack(hero)
  elif user_input == 2:
    print("You just stand there")
    goblin.attack(hero)
  elif user_input == 3:
    print("You choose to flee as the coward you are!")
    break
  elif user_input > 3:
    print("\n**************\nINVALID CHOICE\n**************\n")
    