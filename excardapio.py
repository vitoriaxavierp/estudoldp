print("Boa tarde! Bem-vindo à Smash Burguer.")
NC = input("Digite seu nome: ")
EN = input("Digite seu endereço: ")
CPF = input("Digite seu CPF: ")

class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return f"\nCliente: {self.nome}\nEndereço: {self.endereco}\nCPF: {self.cpf}"

class ItemCardapio:
    def __init__(self):
        self.produtos = [
            {"id": 1, "nome": "x-burguer", "preco": 15.99, "ingredientes": "Pão, carne, queijo"},
            {"id": 2, "nome": "x-salada", "preco": 17.50, "ingredientes": "Pão, carne, queijo, tomate, alface"},
            {"id": 3, "nome": "x-bacon", "preco": 25.75, "ingredientes": "Pão, carne, queijo, bacon"},
            {"id": 4, "nome": "x-egg", "preco": 18.90, "ingredientes": "Pão, carne, queijo, ovo"},
            {"id": 5, "nome": "coca", "preco": 8.50, "ingredientes": "Contém 500ml"},
            {"id": 6, "nome": "suco de laranja", "preco": 13, "ingredientes": "Contém 400ml"},
            {"id": 7, "nome": "suco de maracujá", "preco": 13, "ingredientes": "Contém 400ml"},
            {"id": 8, "nome": "batata frita", "preco": 23, "ingredientes": "Batata, sal, 400g"},
            {"id": 9, "nome": "nuggets", "preco": 25, "ingredientes": "Nuggets, sal, 400g"}
        ]

    def listar_produtos(self):
        print("\nVocê já pode começar a escolher seu pedido! Digite o número do produto ou '0' para parar:")
        for produto in self.produtos:
            print(f"{produto['id']} - {produto['nome']} | R${produto['preco']:.2f}")

    def obter_produto(self, id_produto):
        for produto in self.produtos:
            if produto["id"] == id_produto:
                return produto
        return None

    def mostrar_detalhes(self, id_produto):
        produto = self.obter_produto(id_produto)
        if produto:
            print(f"\nDetalhes do {produto['nome']}:")
            print(f"Ingredientes: {produto['ingredientes']}")
            print(f"Preço: R${produto['preco']:.2f}")
        else:
            print("Produto não encontrado.")

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto):
        if produto:
            self.itens.append(produto)
            print(f"{produto['nome']} foi adicionado ao carrinho!")
        else:
            print("Produto não encontrado.")

    def listar_carrinho(self):
        print("\nItens no carrinho:")
        if not self.itens:
            print("Carrinho vazio!")
        else:
            total = 0
            for item in self.itens:
                print(f"{item['nome']} | R${item['preco']:.2f}")
                total += item["preco"]
            print(f"Total: R${total:.2f}")
        return total

class Pagamento:
    def __init__(self):
        self.meios = [
            {"id": 1, "tipo": "Pix"},
            {"id": 2, "tipo": "Cartão de Crédito"},
            {"id": 3, "tipo": "Cartão de Débito"},
            {"id": 4, "tipo": "Dinheiro"},
        ]

    def listar_meios(self):
        print("\nQual é o método de pagamento que deseja utilizar:")
        for meio in self.meios:
            print(f"{meio['id']} - {meio['tipo']}")

    def obter_meio(self, id_meio):
        for meio in self.meios:
            if meio["id"] == id_meio:
                return meio
        return None

cliente = Cliente(NC, EN, CPF)
cardapio = ItemCardapio()
carrinho = Carrinho()
pagamento = Pagamento()

print(cliente)

while True:
    cardapio.listar_produtos()
    escolha = input("\nDigite o número do produto para adicioná-lo ao carrinho ou 'D' para ver detalhes. (0 para finalizar): ")

    if escolha == "0":
        break
    elif escolha.lower() == "d":
        id_detalhe = int(input("Digite o número do produto para ver os detalhes: "))
        cardapio.mostrar_detalhes(id_detalhe)
    else:
        try:
            produto_selecionado = cardapio.obter_produto(int(escolha))
            carrinho.adicionar_item(produto_selecionado)
        except ValueError:
            print("Entrada inválida. Tente novamente.")

print()
total_compra = carrinho.listar_carrinho()
pagamento.listar_meios()

while True:
    try:
        metodo_pagamento = int(input("\nEscolha o método de pagamento pelo número: "))
        meio_selecionado = pagamento.obter_meio(metodo_pagamento)

        if meio_selecionado:
            print(f"\nVocê escolheu: {meio_selecionado['tipo']}")
            if meio_selecionado["tipo"] == "Cartão de Crédito":
                parcelas = int(input("Deseja parcelar? Digite de 1 a 3: "))
                if 1 <= parcelas <= 3:
                    valor_parcela = total_compra / parcelas
                    print(f"Compra parcelada em {parcelas}x de R${valor_parcela:.2f}")
                else:
                    print("Número de parcelas inválido, pagamento será feito à vista.")
            break
        else:
            print("Método de pagamento inválido, tente novamente.")
    except ValueError:
        print("Digite um número válido.")

print("\nPedido finalizado! Obrigado por comprar na Smash Burguer.")
