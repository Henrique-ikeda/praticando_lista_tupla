lista = ['Ana', 'João', 'Pedro']

nome_errado = input("Digite o nome incorreto:")
nome_certo = input("Digite o nome correto: ")

if nome_errado in lista:
    posicao = lista.index(nome_errado)

lista[posicao] = nome_certo

print(f"O nome {nome_certo} foi substituido por {nome_errado}")
print(lista)
