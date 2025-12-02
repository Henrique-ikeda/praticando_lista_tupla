lista_inicial = ['Ana', 'Pedro', 'Carlos']
print(f'Lista atual de convidados:{lista_inicial}')
nome = input("Digite o nome do novo convidado:")
posicao = int(input("Digite a posição na qual deseja inserir o convidado:"))

lista_inicial.insert(posicao - 1, nome)
print(f"Lista atualizada de convidados:{lista_inicial}")
