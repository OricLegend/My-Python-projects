import random
winning_no = random.randint(1,100)

# winning_no = 76

guess = 1

guessing_no = int(input("enter any no b/w 1 to 100 : "))

game_over = False
while not game_over:
    if winning_no == guessing_no:
        print(f"You win !! and you guessed this no in {guess} times")
        game_over = True
    else:
        if guessing_no < winning_no:
            print("too low")
            
        else:
            print("too high")
            
        guessing_no = int(input("Guess again : "))
        guess += 1

