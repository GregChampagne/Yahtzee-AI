import random
import scoring

dice = [1, 1, 1, 1, 1]
protect = [0, 0, 0, 0, 0]
rolls = 0
more = True
s = scoring.Score()


# Roll the 5 dice, then ask nicely for them to be sorted
def take_turn():
    for i in range(0, 5):
        if protect[i] == 0:
            dice[i] = random.randint(1, 6)
    sort_dice()
    print(dice)


# Sort the dice and set the die array to the sorted version
def sort_dice():
    dice_temp = sorted(dice)
    for i in range(0, 5):
        dice[i] = dice_temp[i]


# Choose whether or not to protect each die
def choose_dice():
    print("0 For no, 1 for Yes")
    for i in range(0, 5):
        choice = int(input("Keep die " + str(i + 1) + "? "))
        protect[i] = choice


# Handles the choice of which option to fill out, with some protections
def decision():
    s.print_options()
    correct_choice = False
    while not correct_choice:
        choice = int(input("Pick an open slot! "))
        if choice < 7:
            if s.upper_scores[choice - 1] == -1:
                correct_choice = True
                s.score_upper(choice, dice)
        elif choice < 13:
            if s.lower_scores[choice - 7] == -1:
                correct_choice = True
                s.score_lower(choice - 7, dice)
        else:
            if s.yahtzee_score == -1:
                correct_choice = True
                s.score_yahtzee(dice)
        for i in range(0, 5):
            protect[i] = 0

# Main Game loop
while more:
    take_turn()
    rolls += 1
    if rolls != 3:
        choose_dice()
    else:
        decision()
        rolls = 0
        s.print_options()
