from Warrior import Warrior
from Mage import Mage 
from EvilWizard import EvilWizard
from Saint import Saint
from Assassin import Assassin

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Assassin") 
    print("4. Saint")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ").capitalize()

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Assassin(name)
    elif class_choice == '4':
        return Saint(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")


        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.ability_choice(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if choice != '2' and wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
        
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

