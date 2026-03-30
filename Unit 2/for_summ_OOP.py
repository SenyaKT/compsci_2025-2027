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
    rounds=0
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
        Character.rounds+=1
        new_health=self.__health - damage
        self.setheath(new_health)
    def is_alive(self):
        return self.__health>0

hero=Character("Aka",100,35)
monster=Character("Killer",110,25)

while hero.is_alive() and monster.is_alive():
    monster.take_damage(hero.getbasic_attack())
    print(Character.rounds, monster.getname() ,"being attacked by",hero.getname(),"damage:", hero.getbasic_attack(),"health left:", monster.gethealth() )

    if not monster.is_alive():
        break
    
    hero.take_damage(monster.getbasic_attack())
    print(Character.rounds , hero.getname() ,"being attacked by",monster.getname(),"damage:", monster.getbasic_attack(),"health left:", hero.gethealth() )

if not monster.is_alive():
    print(f"The winner is {hero.getname()}")
else:
    print(f"The winner is {monster.getname()}")



