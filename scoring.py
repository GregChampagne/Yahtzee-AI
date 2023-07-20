


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
        print("13. Yahtzee! " + str(self.yahtzee_score))

    def score_upper(self, c, d):
        subscore = 0
        for i in range(0, 5):
            if c == d[i]:
                subscore += c

        self.upper_scores[c - 1] = subscore
        self.print_options()

    def score_lower(self, c, d):
        counts = [0, 0, 0, 0, 0, 0]
        num_sum = 0
        max_of_kind = 1
        for i in range(0, 5):
            if d[i] == 1:
                counts[0] += 1
            elif d[i] == 2:
                counts[1] += 1
            elif d[i] == 3:
                counts[2] += 1
            elif d[i] == 4:
                counts[3] += 1
            elif d[i] == 5:
                counts[4] += 1
            elif d[i] == 6:
                counts[5] += 1
            num_sum += d[i]

        for i in range(0, 5):
            if counts[i] > max_of_kind:
                max_of_kind = counts[i]

        # Three of a Kind
        if c == 0:
            if self.lower_scores[c] == -1:
                if max_of_kind >= 3:
                    self.lower_scores[c] = num_sum
                else:
                    self.lower_scores[c] = 0

        # Four of a Kind
        if c == 1:
            if self.lower_scores[c] == -1:
                if max_of_kind >= 4:
                    self.lower_scores[c] = num_sum
                else:
                    self.lower_scores[c] = 0

        # Full House
        if c == 2:
            full_house = False
            if self.lower_scores[c] == -1:
                if max_of_kind == 3:

                    for i in range(0, 5):
                        if counts[i] == 2:
                            full_house = True

                if full_house:
                    self.lower_scores[c] = 25
                else:
                    self.lower_scores[c] = 0

        # Small Straight
        if c == 3:
            score = 0
            if self.lower_scores[c] == -1:
                if counts[0] > 0 and counts[1] > 0 and counts[2] > 0 and counts[3] > 0:
                    score = 30
                elif counts[1] > 0 and counts[2] > 0 and counts[3] > 0 and counts[4] > 0:
                    score = 30
                elif counts[2] > 0 and counts[3] > 0 and counts[4] > 0 and counts[5] > 0:
                    score = 30
                self.lower_scores[c] = score

        # Large Straight
        if c == 4:
            score = 40
            if self.lower_scores[c] == -1:
                for i in range(1, 5):
                    if d[i] != (d[i-1] + 1):
                        score = 0

                self.lower_scores[c] = score

        # Chance
        if c == 5:
            if self.lower_scores[c] == -1:
                self.lower_scores[c] = num_sum

    def score_yahtzee(self, d):
        num = d[0]
        yahtzee = True
        for i in range(1, 5):
            if d[i] != num:
                yahtzee = False

        if yahtzee:
            if self.yahtzee_score == -1:
                self.yahtzee_score = 50
            else:
                self.yahtzee_score += 100
        else:
            self.yahtzee_score = 0

