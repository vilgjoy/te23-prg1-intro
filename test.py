# Detta är bara för att testa klasser, behöver inte se detta. algoritim.py är uppgiften.
class Player: 
    # Instead of making new variables every time, you can make a class to make the next smoother
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100 # Amount of exp needed for next lvl
        self.abilities = []

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
        new_abilities = {
            2: "Fireball" ,
            3: "Healing" ,
            5: "Lightning strike"
        }
        if self.level in new_abilities:
            ability = new_abilities[self.level]
            self.abilities.append(ability)
            print(f"{self.name} unlocked a new ability: {ability}")

    def display_status(self):
        print(f"Player: {self.name}, XP: {self.xp}/{self.xp_to_next_level}")


player = Player(input("Whats your name?: "))
player.earn_xp(120)
player.display_status()
