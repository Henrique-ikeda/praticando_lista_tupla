lista_comprada = ["maca"]


def verificador():
    item = input("Digite o item que você quer verificar:")
    if item in lista_comprada:
        print("Item comprado.")
    else:
        print(f"O item {item} precisa ser comprado.")
