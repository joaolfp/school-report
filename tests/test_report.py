import unittest
from src.report import Report

class TestReport(unittest.TestCase):

    def test_math_total(self):
        report = Report('João Lucas')
        total = report.math_total(8.0, 2.0, 4.0, 5.0)
        self.assertEqual(total, 19.0)

    def test_english_total(self):
        report = Report('João Lucas')
        total = report.english_total(8.0, 10.0, 4.0, 5.0)
        self.assertEqual(total, 27.0)

    def test_total_notes_success(self):
        report = Report('João Lucas')
        totalMath = report.math_total(8.0, 2.0, 4.0, 5.0)
        totalEnglish = report.english_total(8.0, 10.0, 4.0, 5.0)
        
        result = report.total_notes(totalMath, totalEnglish)
        self.assertEqual(result, '🔥 você foi aprovado')

    def test_total_notes_failed(self):
        report = Report('João Lucas')
        totalMath = report.math_total(0.0, 2.0, 0.0, 1.0)
        totalEnglish = report.english_total(0.0, 10.0, 1.0, 2.0)
        
        result = report.total_notes(totalMath, totalEnglish)
        self.assertEqual(result, '😭 infelizmente você foi reprovado')

if __name__ == '__main__':
    unittest.main()