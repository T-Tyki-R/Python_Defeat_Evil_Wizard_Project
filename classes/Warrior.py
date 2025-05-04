from Character import Character
import random
import math

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=25)

         # A Defense/Evade Function
    def ability1(self, opponent, ability="Perfect Guard"):
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
    def ability2(self, opponent, ability = "Justly Slash"):
        dmg_dealt = random.randint(20, 30)
        sim_dmg = random.randint(10, opponent.attack_power)
        # Deal damage to opponent
        opponent.health -= dmg_dealt
        print(f"{self.name} attacked {opponent.name} with {ability}, dealing {sim_dmg} damage!")
        print(f"{opponent.name} attacked {self.name}, dealing {opponent.attack_power}")
        opponent.regenerate()

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # User Choice Function
    def ability_choice(self, opponent):
        print("1. Perfect Guard (Defense)\n2. Justly Slash (Offense)")
        try:
            user_choice = int(input("Which ability do you want to use? "))
            if user_choice == 1:
                self.ability1(opponent)
            elif user_choice == 2:
                self.ability2(opponent)
            else:
                # Only print invalid choice if the opponent is still alive
                if opponent.health > 0:
                    print("Invalid choice! Enter either 1 or 2...")
        except ValueError:
            # Only print invalid input if the opponent is still alive
            if opponent.health > 0:
                print("Invalid input! Please enter a number.")
