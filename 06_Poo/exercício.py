# Atividade
#1.Cahorro
class cachorro:
    def __init__ (self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(self.nome, " diz: Au au!")

    def mostrarinfo(self):
        print("Nome: ", self.nome)
        print("Raça: ", self.raca)
        print("idade: ", self.idade, "\n")


cachorro1 = cachorro("Bidu", "Bordercollie", 49)
cachorro2 = cachorro("Ibiri", "Ibirama", 2)

cachorro1.latir()
cachorro1.mostrarinfo()

cachorro2.latir()
cachorro2.mostrarinfo()

cachorro1.idade = 94
cachorro1.mostrarinfo()

#2. Livro
class Livro:
    def __init__ (self, titulo, autor, qtd_paginas):
        self.titulo = titulo
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.pag_lidas = 0

    def ler(self, paginas):
        self.paginasLidas = min(self.paginasLidas + paginas, self.qtd_paginas)

    def porcentagem_lida(self):
        return self.pag_lidas / (self.qtd_paginas * 100)

    def paginas_restantes(self):
        return self.qtd_paginas - self.pag_lidas

    def terminou(self):
       return self.paginasLidas == self.totalPaginas

livro1 = Livro("A ilha do Tesouro", "Robert Louis Stevenson", 240)
livro1.ler(32)
print(livro1.porcetagem_lida())
print(livro1.paginas_restantes())
print(livro1.terminou())

livro2 = Livro("Arsene Lupin","Maurice Leblanc", 192)
livro2.ler(14)
print(livro2.porcetagem_lida())
print(livro2.paginas_restantes())
print(livro2.terminou())

#3. Conta Bancária

class ContaBancaria:
    def __init__ (self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = 0

    def depositar(self, valor):
        self.saldo_inicial += valor
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo_inicial:
            self.saldo_inicial -= valor

    def extrato(self):
        return f"\nTitular: {self.titular}, Saldo: {self.saldo_inicial}"

conta1 = ContaBancaria("Francisco", "")
conta1.depositar(900)
conta1.sacar(100)
print(conta1.extrato())

conta2 = ContaBancaria("Ibira", "500")
conta2 = conta2.depositar(400)
conta2.sacar(900)
print(conta2.extrato())


#4. Personagem de vieogame

class Personagem:
    def __init__ (self, nome, classe, vida, nivel):
        self.nome = nome
        self.classe = classe
        self.vida = 200
        self.nivel = 1

    def receber_dano(self, valor):
        valor -= self.vida
        if valor >= self.vida:
            print("You Died")

    def cura(self, valor):
        self.vida = min(self.vida + valor, self.vida)

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100

    def status(self):
        print(self.nome, "\n", self.classe, "\n", self.vida, "\n", self.nivel, "\n",)

personagem1 = Personagem("Zodai", "Espadachim", 100)
personagem1.receber_dano(74)
personagem1.cura(30)
personagem1.subir_nivel(1)
personagem1.status()

persongem2 = Personagem("Saitama_careca", "Guerreiro", 100)
persongem2.receber_dano(100)
persongem2.cura(30)
persongem2.status()

#5. Lista de compras (Desafio)

class Produto:
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def subTotal(self):
        return self.preco * self.quantidade
    def mostrar(self):
        return f"\nNome: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\nSubtotal: {self.subTotal():.2f}"

class Carrinho:
    def __init__ (self):
        self.itens = []
    def adicionar(self, Produto):
        self.itens.append(Produto)
        return "\nProduto adicionado com sucesso!"
    def total(self):
        total = 0

        for i in self.itens:
            total += i.subTotal()
        return f"\nTotal: {total}"

    def mostrar(self):
        for i in self.itens:
            print(i.mostrar())
            print(i.subTotal())
        print(self.total())
produto1 = Produto("Abacate", 5, 5)
produto2 = Produto("Banana", 3, 10)
produto3 = Produto("Abacaxi", 8, 9)
produto4 = Produto("Laranja", 4, 2)
carrinho = Carrinho()
carrinho.adicionar(produto1)
carrinho.adicionar(produto2)
carrinho.adicionar(produto3)
carrinho.adicionar(produto4)
print(carrinho.total())
carrinho.mostrar()

