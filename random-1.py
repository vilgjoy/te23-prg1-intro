# Spelet är - Bestäm om det är udda eller jämnt
# rulla tärningar - (computer och player)
# vinnaren är om du hade gissat rätt
from random import randint
rule = input("odd or even, choose one: ")
computer = randint(1,6)
player = randint(1,6)

if rule == "odd":
    # om du hade gissat odd, så hade du vunnit
    computer_result = computer % computer
    player_result = player % computer
    # if computer or player result os 0, number is even
    print(f"The computer rolled {computer_result} and the player rolled {player_result}."
else: # om det inte är odd, så kommer du att förlora 