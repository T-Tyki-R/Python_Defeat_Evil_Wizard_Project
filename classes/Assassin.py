from Character import Character
import random
import math

# Assassin class (inherits from Character)
class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=35)
    
     # A Defense/Evade Function
    def ability1(self, opponent, ability="Lunar Ray"):
        sim_dmg = random.randint(5, opponent.attack_power)
        # Player takes 25% of the attack damage dealt to them if evade fails
        dmg_taken = int(math.floor(sim_dmg * 0.25))
        # Evade success rate is 50%
        evade_chance = random.random() < 0.5
        if evade_chance:
            print(f"{opponent.name} launched his attack!")
            print(f"{self.name} successfully evaded the attack from {opponent.name} using {ability}!")
            print(f"No damage taken. Current health: {self.health}")
            opponent.regenerate()
            print(f"Current health: {self.health}")
        else:
            self.health -= dmg_taken
            print(f"{opponent.name} launched his attack!")
            print(f"{self.name} failed to evade and defend, taking {dmg_taken} damage!")
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
    
    # An Offensive Function
    def ability2(self, opponent, ability = "Silent Night"):
        dmg_dealt = random.randint(20, 30)
        # Deal damage to opponent
        opponent.health -= dmg_dealt
        print(f"{self.name} attacked {opponent.name} with {ability}, dealing {dmg_dealt} damage!")
        print(f"{opponent.name} attacked {self.name}, dealing {opponent.attack_power}")
        opponent.regenerate()

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # User Choice Function
    def ability_choice(self, opponent):
        print("1. Moonlite Lurk (Defense)\n2. Silent Night (Offense)")
        # Error Handling
        try:
            user_choice = int(input("Which ability do you want to use? "))
            if user_choice == 1:
                self.ability1(opponent)
            elif user_choice == 2:
                self.ability2(opponent)
            else:
                print("Invalid choice! Enter either 1 or 2...")
        except ValueError:
            print("Invalid input! Please enter a number.")

