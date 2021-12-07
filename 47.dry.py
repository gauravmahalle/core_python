#dry=don't repeat yourself
winning_number=43
guess=1
number=int(input("guess a number 1 to 100 "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you winn, guess number {guess} time")
        game_over=True

    else:
        if number<winning_number:
            print("too low")
        else:
            print("too high")
    guess+=1
    number=int(input("type again "))