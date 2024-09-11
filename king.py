#Ett spel där två spelare man kastar var sin tärning och den som får högst vinner

# Uppreppa tills vi en person har vunnit tre gånger, den har vunnit allt

from random import randint

play_game = "J"
player_one_score = 0 # värdet börjar på 0 
player_two_score = 0

while play_game.upper() == "J":
    player_one_roll = randint(1,6)
    player_two_roll = randint(1,6)

    if player_one_roll > player_two_roll:
        print(f"Player one won with the roll: {player_one_roll}. Player two got: {player_two_roll}")
        player_one_score += 1
    elif player_two_roll >player_one_roll:
        print(f"Player two won with the roll: {player_two_roll}. Player one got: {player_one_roll}")
        player_two_score += 1
    else:
        print(f"No player won, it's a tie with the rolls: {player_one_roll}")

    play_game = input("Want to play again? [J/N]: ")

# att göra, komma ihåg vilken spelare som vann
# spela tills vi har en bäst av tre
# sedan fråga om vi vill spela igen