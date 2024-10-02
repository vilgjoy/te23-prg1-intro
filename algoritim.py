
from random import randint 

player_one = input("What is your name?")
# choose_class = input("Choose your class: Knight, Thief, Paladin, Cleric, Mage")

player_one_life = 10
player_two_life = 10
game_round = 0
play_again = "Y"

while play_again.upper() == "Y":
    game_round += 1
    print(f"Round {game_round}")
    player_one_roll = randint(1,6)
    player_two_roll = randint(1,6)

    if player_one_roll > player_two_roll:
        player_two_life -= randint(1,3)
        print(f"Player two got stabbed by {player_one}, they have {player_two_life} HP left")
    elif player_two_roll > player_one_roll:
        player_one_life -= randint(1,3)
        print(f"{player_one} got hit by an arrow by Player two, they have {player_one_life} HP left")
    else:
        print(f"{player_one} and Player two is at a standoff, exhaustion gripping the two of them like a dagger.")

    
    if player_two_life <= 0: 
        print(f"After a longfought battle, {player_one} grabs their dagger and finishes off Player two. They raise a fist up in the air in victory, knowing they were stronger.")
       
    elif player_one_life <= 0:
        print(f"After a longfought battle, Player two grabs their dagger and finishes off {player_one}. They raise a fist up in the air in victory, knowing they were stronger.")
        
        
    
    play_again = input("Want to play again? [Y/N]")

# Göra klart extra sakerna
# Göra så spelet slutar




