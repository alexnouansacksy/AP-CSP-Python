class node:
    def __lt__(self, other):
        return self.score < other.score
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def getScore(self):
        return self.score

    def setScore(self, newScore):
        self.score = newScore
    def __str__(self):
        return f"{self.id}\t{self.score}"


