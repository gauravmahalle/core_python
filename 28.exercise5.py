#in this exercise we use NESTED IF ELSE
winning_number=40
guess_number=int(input("guess a number between 1 to 100:"))
if guess_number==winning_number:
    print("you are win")
else:
    if guess_number<winning_number:
        print("to low")
    else:
        print("to high")
