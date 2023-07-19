import random
import scoring

dice = [1, 1, 1, 1, 1]
protect = [0, 0, 0, 0, 0]
rolls = 0
more = True
s = scoring.Score()


def take_turn():
    for i in range(0, 5):
        if protect[i] == 0:
            dice[i] = random.randint(1, 6)
    print(dice)


def choose_dice():
    print("0 For no, 1 for Yes")
    for i in range(0, 5):
        choice = int(input("Keep die " + str(i + 1) + "? "))
        protect[i] = choice


def decision():
    s.print_options()
    correct_choice = False
    while not correct_choice:
        choice = int(input("Pick an open slot! "))
        if choice < 7:
            if s.lower_scores[choice - 1] == -1:
                correct_choice = True
                s.score_upper(choice, dice)
        elif choice < 13:
            if s.upper_scores[choice - 7] == -1:
                correct_choice = True
                s.score_lower(choice - 7, dice)
        else:
            if s.yahtzee_score == -1:
                s.score_yahtzee(dice)

while more:
    take_turn()
    rolls += 1
    if rolls != 3:
        choose_dice()
    else:
        decision()
        rolls = 0
