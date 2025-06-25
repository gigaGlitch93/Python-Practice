secretNumber = 8
guessLimit = 3
guessCount = 0

while guessCount < guessLimit:
    guess = int(input("Guess : "))
    guessCount += 1

    if guess == secretNumber:
        print("You Won !")

        break
else:
    print("You lost , Please try again ")