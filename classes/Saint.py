from Character import Character
import random


# Saint class (inherits from Character)
class Saint(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)

        # A Defense/Evade Function
    def ability1(self, opponent, ability="Holy Shine"):
        # Player takes 30% of the attack damage dealt to them if evade fails
        dmg_taken = opponent.attack(self) * 0.3
        # Evade success rate is 50%
        evade_chance = random.random() < 0.5
        if evade_chance:
            print(f"{self.name} successfully evaded the attack from {opponent.name} using {ability}!")
        else:
            self.health -= dmg_taken
            print(f"{self.name} failed to evade and defend, taking {dmg_taken:.2f} damage!")
            if self.health <= 0:
                print(f"{self.name} has been defeated!")
    
    # An Offensive Function
    def ability2(self, opponent, ability = "Righteous Purity"):
        dmg_dealt = random.randint(20, 40)
        # Deal damage to opponent
        opponent.health -= dmg_dealt
        print(f"{self.name} attacked {opponent.name} with {ability}, dealing {dmg_dealt} damage!")

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # User Choice Function
    def ability_choice(self, opponent):
        print("1. Holy Shine (Defense)\n2. Righteous Purity (Offense)")
        # Error Handling
        try:
            user_choice = int(input("Which ability do you want to use? "))
            if user_choice == 1:
                self.ability1(opponent)
            elif user_choice == 2:
                self.ability2(opponent)
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")
