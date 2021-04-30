from report import Report

report = Report('João Lucas')
print('================= Notas do ' + report.name + ' =================')
print('----------------------------------------------')
print('================= Matemática =================')
firstMath = float(input('Nota do primeiro bimestre: '))
secondMath = float(input('Nota do segundo bimestre: '))
threeMath = float(input('Nota do terceiro bimestre: '))
fourMath = float(input('Nota do quarto bimestre: '))

print('----------------------------------------------')
print('================= Inglês =================')
firstEnglish = float(input('Nota do primeiro bimestre: '))
secondEnglish = float(input('Nota do segundo bimestre: '))
threeEnglish = float(input('Nota do terceiro bimestre: '))
fourEnglish = float(input('Nota do quarto bimestre: '))
print('----------------------------------------------')

mathNote = report.math_total(firstMath, secondMath, threeMath, fourMath)
englishNote = report.english_total(firstEnglish, secondEnglish, threeEnglish, fourEnglish)

report.totalNotes(mathNote, englishNote)