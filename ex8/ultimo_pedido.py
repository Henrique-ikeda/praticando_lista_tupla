def remover_ultimo(pedidos):
    pedidos.pop()


pedidos = input("Pedidos feitos (separados por vírgula): ").split(',')
remover_ultimo(pedidos)
print(f"Pedidos finais: {pedidos}")
