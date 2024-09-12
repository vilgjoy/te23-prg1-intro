#Ett spel där två spelare man kastar var sin tärning och den som får högst vinner

# Uppreppa tills vi en person har vunnit tre gånger, den har vunnit allt

# O

from random import randint

play_game = "J"
player_one_score = 0 # värdet börjar på 0 
player_two_score = 0
game_round = 0

dice_sides = int(input("How many sides of the dice do you want?: "))
rounds_total # ändra detta så man kan välja hur många rundor
while play_game.upper() == "J":
    game_round += 1
    player_one_roll = randint(1,dice_sides)
    player_two_roll = randint(1,dice_sides)

    if player_one_roll > player_two_roll:
        print(f"Player one won with the roll: {player_one_roll}. Player two got: {player_two_roll}")
        player_one_score += 1
    elif player_two_roll >player_one_roll:
        print(f"Player two won with the roll: {player_two_roll}. Player one got: {player_one_roll}")
        player_two_score += 1
    else:
        print(f"No player won, it's a tie with the rolls: {player_one_roll}")


    if player_one_score >= 2:
        print(f"Player one won with {player_one_score} points after {game_round} rounds, while Player two got {player_two_score} points")
        play_game = "n"
    elif player_two_score >= 2:
        print(f"Player two won with {player_two_score} points after {game_round} rounds, while Player one got {player_one_score} points")
        play_game = "n"
    elif game_round >= 3: # Om rundan passerat 3, så vinner ingen
        print(f"{game_round} turns have passed and no player has won. Player one has {player_one_score} pointsand player two has {player_two_score}points ")
    
    play_game = input("Want to play again? [J/N]: ")

# att göra, komma ihåg vilken spelare som vann
# spela tills vi har en bäst av tre
# sedan fråga om vi vill spela igen