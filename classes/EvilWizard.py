from Character import Character
import random
import math

# Evil Wizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=30)

    def regenerate(self):
        # Check if the wizard's current health is above a certain threshold (20 health) before regenerating
        if self.health > 20:
            health_regen = int(math.floor(random.randint(20, self.health) * .1 )) # Regenerate 10% of health)
            # Check if the wizard's health is below a certain threshold before regenerating
            if self.health < 200 and self.health + health_regen < 200: 
                self.health += health_regen
                print(f"{self.name} regenerates {health_regen} health! Current health: {self.health}")
            elif self.health <= 0:
                self.health = 0
            else:
                # If health is above the threshold, set it to max health = (200)
                self.health = 200
                print(f"{self.name} has maxed out health! Current health: {self.health}")
        else:
            print(f"{self.name} is too weak to regenerate health!")

