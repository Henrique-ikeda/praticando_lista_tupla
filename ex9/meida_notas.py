notas = input("Digite as notas dos alunos separadas por vírgula:").split(',')
notas = [float(nota) for nota in notas]
media = sum(notas)/len(notas)
print(media)
