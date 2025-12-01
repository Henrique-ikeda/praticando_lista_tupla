texto1 = input("Produtos do estoque 1 (separados por vírgula):")
texto2 = input("Produtos do estoque 2 (separados por vírgula):")

tupla = tuple(texto1.split(',') + texto2.split(','))
print(tupla)
