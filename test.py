# Detta är bara för att testa klasser, behöver inte se detta. algoritim.py är uppgiften.
from random import randint
class Opponent:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, player):
        # Opponent attacks player
        damage = randint.(10,25)
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        return damage
    
class Player: 
    # Instead of making new variables every time, you can make a class to make the next smoother
    def __init__(self, name, health):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100 # Amount of exp needed for next lvl
        self.abilities = []
        self.health = health # Player health
    
    def choose_action(self):
        # Player choose a action if they start the turn
        print("You got the upper hand")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Magic")
        print("4. Use Skill")

        choice = input("[1. 2. 3. 4.] ")

        if choice == "1":
            return "attack"
        elif choice == "2":
            return "defend"
        elif choice == "3":
            return "use magic"
        elif choice == "4":
            return "use skill"
        else:
            return "attack"
    
    def attack(self, opponent):
        # Player attacks the opponent
        damage = randint(10,30)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        return damage
    
    def defend(self):
        # Player defends, reducing damage
        print(f"{self.name} is concentrated, incoming damage is reduced by half!")
        return 0.5 # Reduces incoming damage by half (damage * 0.5 = damage / 2)
    
    def use_magic(self, opponent):
        # Player uses their magic to attack
        magic_damage = randint(20,40)
        print(f"{self.name} fills their mana onto {opponent.name} for {magic_damage} damage!")
        return magic_damage
    
    def use_skill(self, opponent):
        # Player uses a skill to attack
        skill_damage = randint(15,35)
        print(f"{self.name} fills their aura onto {opponent.name} for {skill_damage} damage!")
        return skill_damage

    def earn_xp(self, amount): # Player earns xp when this function is used
        self.xp += amount
        print(f"{self.name} earned {amount} XP")

        if self.xp >= self.xp_to_next_level:
            self.level_up()
    
    def level_up(self): 
        self.level += 1
        self.xp -= self.xp_to_next_level # Reset XP, carry over excess XP
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5) # Increase XP needed for next lvl
        print(f"{self.name} leveled up to level {self.level}")
        print(f"XP to next level: {self.xp_to_next_level}")
        self.unlock_abilities()
    
    def unlock_abilities(self):
        if self.level == 2 and "Fireball" not in self.abilities:
            self.abilities.append("Fireball")
            print(f"{self.name} has unlocked Fireball")
        elif self.level == 3 and "Healing" not in self.abilities:
            self.abilities.append("Healing")
            print(f"{self.name} has unlocked Healing")
        elif self.level == 5 and "Lightning Strike" not in self.abilities:
            self.abilities.append("Lightning Strike")
            print(f"{self.name} has unlocked Lightning Strike")

    def display_status(self):
        print(f"Player: {self.name}, XP: {self.xp}/{self.xp_to_next_level}")
        
def combat(player, opponent):
    # Combat between player and enemy
    turn = randint.choice(["player", "opponent"]) # 50/50 chance who goes first
    print(f"The {turn} shall begin the fight!")

    while player.health > 0 and opponent.health > 0:
        if turn == "player":
            print("\n--- Player's Turn ---")
            action = player.choose_action()

            if action == "attack":
                damage = player.attack(opponent)
                opponent.health -= damage
            elif action == "defend":
                defense_modifier = player.defend()
            elif action == "magic":
                damage = player.use_magic(opponent)
                opponent.health -= damage
            elif action == "skill":
                damage = player.use_skill(opponent)
                opponent.health -= damage
                
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated")
                break

            turn = "opponent" # Switch to enemy turn
            
        else:
            print("\n--- Opponent's Turn")
            damage = opponent.attack(player)

            if 'defense_modifier' in locals():
                damage *= defense_modifier # Apply defense modifier if player defended the previous turn
                del defense_modifier # Reset defense modifier after use
                
            player.health -= damage

            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                break

            turn = "player" # Switch to players turn

        print(f"\n{player.name}'s health: {player.health}")
        print(f"{opponent.name}'s health: {opponent.health}")


player = Player(input("Whats your name?: "), 100)
opponent = Opponent("Goblin", 80)
combat =(Player, Opponent)
player.earn_xp(120)
player.display_status()
