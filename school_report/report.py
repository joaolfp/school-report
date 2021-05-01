from math_subject import MathSubject
from english_subject import EnglishSubject

class Report(object):

    def __init__(self, name):
        self.name = name

    def math_total(self, first, second, three, four):
        math = MathSubject()
        return float(math.first_note(first) + math.second_note(second) + math.three_note(three) + math.four_note(four))

    def english_total(self, first, second, three, four):
        english = EnglishSubject()
        return float(english.first_note(first) + english.second_note(second) + english.three_note(three) + english.four_note(four))

    def total_notes(self, math, english):
        total = (math + english) / 2

        if total >= 20:
            return '🔥 você foi aprovado'
        else:
            return '😭 infelizmente você foi reprovado'