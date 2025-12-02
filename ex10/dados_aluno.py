
aluno = input(
    "Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula:").split(',')


for i in range(0, len(aluno), 3):
    nome, idade, nota = aluno[i], int(aluno[i + 1]), float(aluno[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
