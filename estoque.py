class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
    
    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print("Estoque insuficiente!")

    def __str__(self):
        return f'Produto: {self.nome}, Preço: {self.preco:.2f}, Quantidade: {self.quantidade}'

# Função principal para executar o sistema
def main():
    p1 = Produto("Caderno", 15.99, 50)
    p2 = Produto("Caneta", 2.49, 100)

    print(p1)
    print(p2)

    p1.vender(5)
    p2.adicionar_estoque(20)

    print("\nApós vendas e atualização de estoque:")
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()

