
from random import randint 

player_one = input("What is your name player one?: ")
player_one_class = input("Pick your class: [Rogue or Fighter] ")
# Rogue gets to reroll if they lose the dice roll and has a 20% to deal extra dmg
# Fighter either gain a certain amount of HP or loses HP when they lose the dice roll and deals extra dmg depending on their missing HP
# Paladin wins the dice roll, they can choose to debuff player two and buff themself
# Clerics deal continues holy dmg instead of regular dmg and it stacks every time they win the dice roll.
player_two = input("What is your name player two?: ")

if player_two == "":
    player_two = "Computer"


player_one_life = 10
player_two_life = 10
game_round = 0
play_again = "Y"
player_one_lvl = 1
player_one_exp = 0
exp_next_lvl = 100
def earn_exp(amount):
    player_one_exp += amount
    print(f"{player_one} earned {amount} XP")

    # If the player leveled up
    if player_one_exp >= exp_next_lvl:
        player_one_up()

def player_one_up(): 
    player_one_lvl += 1
    # Excess exp points
    player_one_exp -= exp_next_lvl
    exp_next_lvl = int(exp_next_lvl * 1.5)
    print(f"{player_one} leveled up to level {player_one_lvl}")
    print(f"XP to next level: {exp_next_lvl}")
while play_again.upper() == "Y":
    player_one_life = 10
    player_two_life = 10
    game_round = 0
    play_again = "Y"
    crit_chance = 0.25
    crit_mult = 2.0
    while player_one_life > 0 and player_two_life > 0:
        game_round += 1
        print(f"Round {game_round}")
        player_one_roll = randint(1,6)
        player_two_roll = randint(1,6)
        

        if player_one_roll > player_two_roll and player_one_class == "Rogue":
            player_one_dmg = randint(2,7)
            player_two_dmg = randint(1,6)
            if player_one_dmg > player_two_dmg:
                player_two_life -= (player_one_dmg - player_two_dmg)
                print(f"{player_two} got stabbed by {player_one}, they have {player_two_life} HP left")
            else:
                 print(f"{player_one} got the upper hand and pushed {player_two}, leaving {player_two} at a dissavantage")

        elif player_two_roll > player_one_roll and player_one_class == "Rogue":
            player_one_roll = randint(1,6)
            if player_one_roll > player_two_roll:
                player_one_dmg = randint(1,6)
                player_two_dmg = randint(1,6)
                if player_one_dmg > player_two_dmg:
                    player_two_life -= (player_one_dmg - player_two_dmg)
                    print(f"{player_two} got hit by an arrow by {player_one}, they have {player_two_life} HP left")
            elif player_two_roll > player_one_roll:
                player_one_dmg = randint(1,6)
                player_two_dmg = randint(1,6)
                if player_two_dmg > player_one_dmg:
                    player_one_life -= (player_two_dmg - player_one_dmg)
                    print(f"Even if {player_one} got the advantage, {player_two} got the upper hand and sliced {player_one} so they have {player_one_life} health left")
            else:
                 print(f"{player_two} got the upper hand and pushed {player_one}, leaving {player_one} at a dissavantage")



        if player_one_roll > player_two_roll and player_one_class == "Fighter":
            player_one_dmg = randint(1,5)
            player_two_dmg = randint(1,6)
            if player_one_dmg > player_two_dmg:
                player_two_life -= (player_one_dmg * crit_mult - player_two_dmg)
                print(f"{player_two} got stabbed by {player_one}, they have {player_two_life} HP left")
            else:
                 print(f"{player_one} got the upper hand and pushed {player_two}, leaving {player_two} at a dissavantage")

        elif player_two_roll > player_one_roll and player_one_class == "Fighter":
            player_one_dmg = randint(1,6)
            player_two_dmg = randint(1,6)
            if player_two_dmg > player_one_dmg:
                player_one_life -= (player_two_dmg - player_one_dmg + 1)
                print(f"{player_one} got hit by an arrow by {player_two}, they have {player_one_life} HP left")
            else:
                 print(f"{player_two} got the upper hand and pushed {player_one}, leaving {player_one} at a dissavantage")
                
                
        else:
            print(f"{player_one} and {player_two} is at a standoff, exhaustion gripping the two of them like a dagger.")
        
        
    
        
        if player_two_life <= 0: 
            print(f"After a longfought battle, {player_one} grabs their dagger and finishes off {player_two}. They raise a fist up in the air in victory, knowing they were stronger.")
            player_one_exp += (80 + {game_round})
            if player_one_exp > exp_next_lvl:
                player_one_lvl += 1
                print(f"{player_one} level increased to lvl {player_one_lvl}")
            play_again = "N"
        elif player_one_life <= 0:
            print(f"After a longfought battle, {player_two} grabs their dagger and finishes off {player_one}. They raise a fist up in the air in victory, knowing they were stronger.")
            play_again = "N"
            
    
    play_again = input("Want to play again? [Y/N]")

# Göra klart extra sakerna
# Göra så spelet slutar




