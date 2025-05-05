class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho.")

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f"Produto '{nome_produto}' removido do carrinho.")
                return
        print(f"Produto '{nome_produto}' não encontrado no carrinho.")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total

    def mostrar_carrinho(self):
        if not self.produtos:
            print("Carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f" - {produto}")
            print(f"Total: R$ {self.calcular_total():.2f}")


p1 = Produto("Camisa", 50.00)
p2 = Produto("Calça", 120.00)
p3 = Produto("Boné", 30.00)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

carrinho.mostrar_carrinho()

carrinho.remover_produto("Calça")
carrinho.mostrar_carrinho()
