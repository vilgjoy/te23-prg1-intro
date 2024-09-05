from random import randint
# Man ska gissa ett tal och om du gissar rätt, vinner du

guess = 0
answer = randint(1,10)
while guess != answer:
    guess = int(input("Gissa ett tal mellan 1 och 10: "))
    if guess > answer:
        print("Du gissade för högt")
    elif guess < answer:
        print("Du gissade för lågt")
    else:
        print("Du vann")