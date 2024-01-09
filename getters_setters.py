

class Game:

    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score


onj = Game()
print(onj.score)

onj.score = 20
print(onj.score)