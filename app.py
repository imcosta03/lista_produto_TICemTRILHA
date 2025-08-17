
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

def remover_produto():
    try:
        remover_id = int(input("Digite o ID para remover o produto: "))
    except ValueError:
        print("ID inválido, tente novamente!")
        return
    
    for produto in lista_compras:
        if produto["id"] == remover_id:
            lista_compras.remove(produto)
            print(f"ID do produto não encontrado")

def mostrar_produto():
    if not lista_compras:
        print("Lista zerada, Digite A para adicionar")
    else:
        print(f"{'ID':<5} {'Nome':<15} {'Unid':<6} {'Qtd'}")
        print("-"*42)
        for produto in lista_compras:
            print(f"{produto['id']:<5} {produto['nome']:<15} {produto['unidade']:<6} {produto['quantidade']}")

def pesquisar_produto():
    nome_produto = input("Qual produto você está procurando: ").lower()
    encontrados = [p for p in lista_compras if nome_produto in p["nome"].lower()]
    print(f"\n {len(encontrados)} produto(s) encontrado(s): ")
    
    for p in encontrados:
        print(f"ID {p['id']} - {p['nome']} {p['quantidade']}  {p['unidade']}  {p['descricao']}")

def exibir_menu():
    print(f"\n{'*' *7} Programa Lista de Produtos {'*' *7} ") 
    print("""
        [A] Adicionar       [R] Remover
        [P] Pesquisar       [S] Sair
    """)
    print('-'*42)

def escolher_menu():
    while True:
        mostrar_produto()
        exibir_menu()
        opcao = input("Escolha uma opção: ").upper()

        if opcao == "A":
            adicionar_produto()
        elif opcao == "R":
            mostrar_produto()
            remover_produto()
        elif opcao == "P":
            pesquisar_produto()
            continue
        elif opcao == "S":
            print("Agradecemos por utilizar nosso serviço, volte sempre!")
            break
        else: 
            print("Opção invalida")


