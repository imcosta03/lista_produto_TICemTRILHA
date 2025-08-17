
#variaveis global
lista_compras = []
produto_id = 1

unidades = {
    "q":"Quilograma",
    "g":"Grama",
    "l":"Litro",
    "m":"Mililitro",
    "u":"Unidade",
    "c":"Centímetro",
}

def adicionar_produto():
    global produto_id

    nome = input("Nome do produto: ")

    # Validação da unidade
    while True:
        print("\nSelecione a unidade de medida:")
        for letra, palavra in unidades.items():
            print(f"[{letra}] {palavra}")
        unidade_opcao = input("Opção: ").lower()

        if unidade_opcao in unidades:
            unidade = unidade_opcao
            break
        else:
            print("Unidade inválida. Tente novamente.")

    # Validação da quantidade
    while True:
        try:
            quantidade = float(input("Quantidade: "))
            break
        except ValueError:
            print("Quantidade inválida. Digite um número (ex: 2 ou 3.5).")

    descricao = input("Descrição do Produto: ")

    produto = {
        "id": produto_id,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    }

    # Adição de um produto na lista
    lista_compras.append(produto)
    print(f"\nProduto '{nome}' adicionado com sucesso com ID = {produto_id}\n")
    produto_id += 1

adicionar_produto()

