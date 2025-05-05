Python_Defeat_Evil_Wizard_Project

This project focuses on developing a turn-based action game in the terminal using Python. The player will choose a character class and battle the Evil Wizard using strategic actions to defeat the wizard, such as:
1. Basic Attacks
2. Special Abilities
3. Healing
4. Health Monitoring
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Warrior Class (WC)
2. Mage Class  (MC)
3. Assassin Class (AC)
4. Saint Class (SC)
5. Evil Wizard Class (EWC)

Each class focuses on manipulating data via inheritance, method calls, constructors and more.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Outside EWC, the other classes are essentially cookie-cutters/duplicates with minimal customization:

1. Attack Names
2. Attack Power

Each class consists of 3 functions:

1. Ability1() - Defense
   Allows player to evade opponents next attack, but relies on 50/50 probability. If user fails to successfully evade, they'll take minor damage.
3. Ability2() - Offense
   Allows player to attack opponents, dealing massive, but randomized.
5. Ability_Choice() - User Input
  Players must choose either abilities, or will recieve an error for invalid input.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
The EWC consists of a single function, regenerate(), which allows the Evil Wizard to regenate a random amount of health when called.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
