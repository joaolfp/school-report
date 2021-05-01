from report import Report

name = input('Digite o nome do aluno: ')

report = Report(name)
print('=================================================================')
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

print('----------------------------------------------------')
print('----------------------------------------------------')
print('' + report.name + ' seu boletim')

print('✌️ Matemática' + ' - 1 Bimestre ' + '- ' + str(firstMath))
print('✌️ Matemática' + ' - 2 Bimestre ' + '- ' + str(secondMath))
print('✌️ Matemática' + ' - 3 Bimestre ' + '- ' + str(threeMath))
print('✌️ Matemática' + ' - 4 Bimestre ' + '- ' + str(fourMath))
print('=======================================================')
print('🇺🇸 Inglês' + ' - 1 Bimestre ' + '- ' + str(firstMath))
print('🇺🇸 Inglês' + ' - 2 Bimestre ' + '- ' + str(secondMath))
print('🇺🇸 Inglês' + ' - 3 Bimestre ' + '- ' + str(threeMath))
print('🇺🇸 Inglês' + ' - 4 Bimestre ' + '- ' + str(fourMath))

print(report.total_notes(mathNote, englishNote))