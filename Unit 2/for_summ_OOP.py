""""
We’ll create a combat situation for 2 Character objects, simulating how a game would calculate and track object states.

Create a Character class
Define 3 private attributes: name (str), health (int)and basic_attack(int).
Write getters for all attrs
Write a setter for health as it’s the only one that should be changed during gameplay. Health should never be negative, and it should be set to 0 if it’d be negative.
Implement take_damage(damage_amount) method to subtract damage taken from health
Implement is_alive() method that returns True if a character has more than 0 health, False otherwise.
Instantiate 2 Character objects(Hero vs monster, Batman vs Joker etc.)
Write a loop that simulates the battle by making the objects take turns to deal their base_attack value as damage to the other object. This loop should continue until one of them returns False on is_alive() method call.
Print the winner’s name after the loop is over.

"""
#private attributes: __attibute
#protected attributes : _attribute


class Character:
    def __init__(self,name,health,basic_attack):
        self.__name=name
        self.__health=health
        self.__basic_attack=basic_attack
    def getname(self):
        return self.__name
    def gethealth(self):
        return self.__health
    def getbasic_attack(self):
        return self.__basic_attack
    def setheath(self,new_health):
        if new_health<0:
            self.__health=0
        else:
            self.__health=new_health
    def take_damage(self,damage):
        new_health=self.__health - damage
        self.setheath(new_health)
    def is_alive(self):
        return self.__health>0

hero=Character("Aka",100,35)
monster=Character("Killer",110,25)

while hero.is_alive() and monster.is_alive():
    monster.take_damage(hero.getbasic_attack())
    print(monster.getname() ,"being attacked by",hero.getname(),"damage:", hero.getbasic_attack(),"health left:", monster.gethealth() )

    if not monster.is_alive():
        break
    
    hero.take_damage(monster.getbasic_attack())
    print(hero.getname() ,"being attacked by",monster.getname(),"damage:", monster.getbasic_attack(),"health left:", hero.gethealth() )

if not monster.is_alive():
    print(f"The winner is {hero.getname()}")
else:
    print(f"The winner is {monster.getname()}")

--------------------------------------------------

# Character class represents a game character with state (attributes)
# and behaviour (methods)
class Character:
    rounds=0 
    # Constructor initializes the object state
    def __init__(self, name, health, basic_attack):
        self._name = name                # protected attribute: character name
        self._health = health            # protected attribute: health points
        self._basic_attack = basic_attack  # protected attribute: attack damage

    # Getter for name
    def get_name(self):
        return self._name

    # Getter for health
    def get_health(self):
        return self._health

    # Getter for attack value
    def get_basic_attack(self):
        return self._basic_attack

    # Setter for health (only attribute allowed to change)
    # Ensures health never goes below 0
    def set_health(self, new_health):
        if new_health < 0:
            self._health = 0
        else:
            self._health = new_health

    # Method to apply damage to the character
    # Uses setter to ensure validation
    def take_damage(self, damage_amount):
        Character.rounds+=1
        new_health = self._health - damage_amount
        self.set_health(new_health)

    # Method to check if character is still alive
    def is_alive(self):
        return self._health > 0




# Instantiate two Character objects
hero = Character("Batman", 100, 20)
monster = Character("Joker", 80, 15)




# Loop continues while BOTH characters are alive
while hero.is_alive() and monster.is_alive():

    # Hero attacks monster
    monster.take_damage(hero.get_basic_attack())
    print(Character.rounds,hero.get_name(), "attacks!",
          monster.get_name(), "health:", monster.get_health())

    # Check if monster died after attack
    if not monster.is_alive():
        break  # exit loop if monster is dead

    # Monster attacks hero
    hero.take_damage(monster.get_basic_attack())
    print(Character.rounds, monster.get_name(), "attacks!",
          hero.get_name(), "health:", hero.get_health())
    




# After loop ends, determine winner
if hero.is_alive():
    print("Winner is:", hero.get_name())
else:
    print("Winner is:", monster.get_name())