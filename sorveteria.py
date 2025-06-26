# Estoque e preços dos produtos
estoque = {
    "casquinha": 10,
    "sorvete_chocolate": 5,
    "sorvete_morango": 8
}

precos = {
    "casquinha": 2.00,
    "sorvete_chocolate": 5.00,
    "sorvete_morango": 5.00
}

# Exibe o menu com produtos, preços e estoque
def exibir_menu_produtos():
    print("\nProdutos disponíveis:")
    for item, preco in precos.items():
        quantidade = estoque.get(item, 0)
        print(f" - {item} (R${preco:.2f}) - {quantidade} no estoque")
    print("Digite 'fim' quando terminar seu pedido.\n")

# Verifica se há estoque suficiente para todos os itens do pedido
def verificar_estoque(itens):
    for item in itens:
        if estoque.get(item, 0) <= 0:
            return False, item
    return True, None

# Atualiza o estoque após uma venda
def atualizar_estoque(itens):
    for item in itens:
        estoque[item] -= 1

# Calcula o total do pedido
def calcular_total(itens):
    return sum(precos[item] for item in itens)

# Simula o pagamento
def simular_pagamento(valor_total):
    print(f"\nSimulando pagamento de R${valor_total:.2f}...")
    return {"status": "aprovado"}

# Simula a emissão de um cupom fiscal
def simular_emissao_cupom(pedido, total):
    print("\n--- CUPOM FISCAL (SIMULAÇÃO) ---")
    for item in pedido:
        print(f"{item} - R${precos[item]:.2f}")
    print(f"TOTAL: R${total:.2f}")
    print("Status: PAGAMENTO APROVADO")
    print("-------------------------------\n")

# Processo principal de venda
def registrar_venda():
    pedido = []
    exibir_menu_produtos()

    while True:
        item = input("Digite o nome do produto: ").strip().lower()
        if item == "fim":
            break
        elif item in precos:
            pedido.append(item)
            print(f"{item} adicionado ao pedido.")
        else:
            print("Produto inválido! Tente novamente.")

    if not pedido:
        print("Nenhum item selecionado.")
        return

    ok, faltando = verificar_estoque(pedido)
    if not ok:
        print(f"O item '{faltando}' está em falta no estoque.")
        return

    total = calcular_total(pedido)
    pagamento = simular_pagamento(total)

    if pagamento["status"] == "aprovado":
        atualizar_estoque(pedido)
        simular_emissao_cupom(pedido, total)
        print("Venda registrada com sucesso!")
    else:
        print("Pagamento não aprovado.")

# Iniciar o processo de venda
registrar_venda()
