import random
import copy
from collections import Counter


class Hat:
    def __init__(self, **ball):
        self.ball = ball
        self.contents = []

        for k, v in self.ball.items():
            for b in range(v):
                self.contents.append(k)

        self.contents_copy = copy.copy(self.contents)

    def draw(self, n):
        drawn = []

        for r in range(n):
            b = random.choice(self.contents)
            self.contents.remove(b)
            drawn.append(b)
            if len(self.contents) == 0:
                self.contents = copy.deepcopy(self.contents_copy)
        return(drawn)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    num_experiments
    for experiment in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        result = Counter(result)
        chk = True
        hat.contents = copy.deepcopy(hat.contents_copy)

        for k, v in expected_balls.items():
            if result[k] < v:
                chk = False
                break

        if chk:
            matches += 1
    return (matches/num_experiments)


hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
print(experiment(hat=hat, expected_balls={
      "yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100))
