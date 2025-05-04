import random
import math

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # Adjust attack power based on a range betweeen 5 and each classes' respected attack power
        attack_dmg = random.randint(5, self.attack_power)
        opponent.health -= attack_dmg
        print(f"{self.name} attacks {opponent.name} for {attack_dmg} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        return attack_dmg

  

    # Heal method to regenerate health
    def heal(self):
        health_regen = random.randint(25, 40)
        # Check if the player's health is below a certain threshold before healing
        if self.health < 150 and self.health + health_regen < 150: 
            self.health += health_regen
            print(f"{self.name} regenerates {health_regen} health! Current health: {self.health}")
        else:
            # If health is above the threshold, set it to max health = (160)
            self.health = 150
            print(f"{self.name} has maxed out health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
