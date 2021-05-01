from math_subject import MathSubject
from english_subject import EnglishSubject

class Report(object):

    def __init__(self, name):
        self.name = name

    def mathTotal(self, first, second, three, four):
        math = MathSubject()
        return float(math.firstNote(first) + math.secondNote(second) + math.threeNote(three) + math.fourNote(four))

    def englishTotal(self, first, second, three, four):
        english = EnglishSubject()
        return float(english.firstNote(first) + english.secondNote(second) + english.threeNote(three) + english.fourNote(four))

    def totalNotes(self, math, english):
        total = (math + english) / 2

        if total >= 20:
            return '🔥 você foi aprovado'
        else:
            return '😭 infelizmente você foi reprovado'