


class Score:
    def __init__(self):
        self.total = 0
        self.upper = 0
        self.lower = 0
        self.upper_scores = [-1, -1, -1, -1, -1, -1]
        self.lower_scores = [-1, -1, -1, -1, -1, -1]
        self.yahtzee_score = -1

    def check_lower(self):
        sum_lower = 0
        for i in self.lower_scores:
            if i != -1:
                sum_lower += i

        if self.yahtzee_score > -1:
            sum_lower += self.yahtzee_score

        self.lower = sum_lower

    def check_upper(self):
        sum_upper = 0
        for i in self.upper_scores:
            if i != -1:
                sum_upper += i

        self.lower = sum_upper

    def check_total(self):
        self.check_lower()
        self.check_upper()
        self.total = self.lower + self.upper

    def print_options(self):
        print("1. Ones " + str(self.upper_scores[0]) + " 7. 3 Of " + str(self.lower_scores[0]))
        print("2. Twos " + str(self.upper_scores[1]) + " 8. 4 Of " + str(self.lower_scores[1]))
        print("3. Threes " + str(self.upper_scores[2]) + " 9. FH " + str(self.lower_scores[2]))
        print("4. Fours " + str(self.upper_scores[3]) + " 10. Small " + str(self.lower_scores[3]))
        print("5. Fives " + str(self.upper_scores[4]) + " 11. Large " + str(self.lower_scores[4]))
        print("6. Sixes " + str(self.upper_scores[5]) + " 12. Chance " + str(self.lower_scores[5]))
        print("0. Yahtzee! " + str(self.yahtzee_score))

    def score_upper(self, c, d):
        subscore = 0
        for i in range(0, 5):
            if c == d[i]:
                subscore += c

        self.upper_scores[c - 1] = subscore
        self.print_options()



    def score_lower(self, c, d):
        print("x")

    def score_yahtzee(self, d):
        print('x')

