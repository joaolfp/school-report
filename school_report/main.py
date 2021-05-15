from report import Report
from rich.console import Console
from rich.table import Table

while True:
    name = input('Digite o nome do aluno: ')

    report = Report(name)
    print("=================================================================")
    print("================= Notas do " + report.name + " =================")
    print("----------------------------------------------")
    print("================= Matemática =================")
    firstMath = float(input("Nota do primeiro bimestre: "))
    secondMath = float(input("Nota do segundo bimestre: "))
    threeMath = float(input("Nota do terceiro bimestre: "))
    fourMath = float(input("Nota do quarto bimestre: "))

    print('----------------------------------------------')
    print('================= Inglês =================')
    firstEnglish = float(input("Nota do primeiro bimestre: "))
    secondEnglish = float(input("Nota do segundo bimestre: "))
    threeEnglish = float(input("Nota do terceiro bimestre: "))
    fourEnglish = float(input("Nota do quarto bimestre: "))
    print("----------------------------------------------")

    mathNote = report.math_total(firstMath, secondMath, threeMath, fourMath)
    englishNote = report.english_total(firstEnglish, secondEnglish, threeEnglish, fourEnglish)

    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("" + report.name + " seu boletim")

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Disciplina")
    table.add_column("1 Bimestre")
    table.add_column("2 Bimestre")
    table.add_column("3 Bimestre")
    table.add_column("4 Bimestre")

    table.add_row(
        "Matemática",
        str(firstMath),
        str(secondMath),
        str(threeMath),
        str(fourMath)
    )

    table.add_row(
        "Inglês",
        str(firstEnglish),
        str(secondEnglish),
        str(threeEnglish),
        str(fourEnglish)
    )

    console.print(table)

    print(report.total_notes(mathNote, englishNote))

    print("=================================================================")