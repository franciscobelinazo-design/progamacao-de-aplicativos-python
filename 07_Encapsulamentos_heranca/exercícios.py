# Atividades

# 1.
print("Atividade 1:")

class Aluno:
    def __init__ (self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    def definir_nota(self, valor):
        if valor >= 0 and valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida!")

    def situacao(self):
        if self.__nota >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Marina", 6.5)
aluno2 = Aluno("Carlos", 9)

print(aluno1.situacao())
aluno1.definir_nota(15)
aluno1.definir_nota(-2)
aluno1.definir_nota(8)
print(aluno1.nota)
print(aluno1.situacao())

aluno2.definir_nota(5)
print(aluno2.nota)
print(aluno2.situacao())

try:
    aluno1.nota = 10
except AttributeError:
    print("Não é permitido alterar a nota diretamente!")

# 2.
print("\nAtividade 2:\n")

class Cofre:
    def __init__ (self, senha):
        self.__senha = senha
        self.__itens = []
        self.__aberto = False
        self.__tentativas = 0
        self.__bloqueado = False

    def abrir(self, senha):
        if self.__bloqueado:
            print("Cofre bloqueado!")
        elif senha == self.__senha:
            self.__aberto = True
            self.__tentativas = 0
            print("Cofre aberto.")
        else:
            self.__tentativas += 1
            print(f"Senha incorreta! Tentativa {self.__tentativas} de 3.")

            if self.__tentativas == 3:
                self.__bloqueado = True

    def fechar(self):
        self.__aberto = False
        print("Cofre fechado.")

    def guardar(self, item):
        if self.__aberto:
            self.__itens.append(item)
            print(f"{item} guardado.")
        else:
            print("Abra o cofre primeiro!")

    def ver_itens(self):
        if self.__aberto:
            print(f"Itens: {self.__itens}")
        else:
            print("Abra o cofre primeiro!")

cofre = Cofre("1234")

cofre.guardar("Relógio")
cofre.abrir("0000")
cofre.abrir("1234")
cofre.guardar("Relógio")
cofre.ver_itens()
cofre.fechar()
cofre.ver_itens()

cofre.abrir("1")
cofre.abrir("2")
cofre.abrir("3")
cofre.abrir("1234")

# 3.
print("\nAtividade 3:\n")

class Produto:
    def __init__ (self, nome, preco, quantidade = 0):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    def entrada(self, qtd):
        if qtd > 0:
            self.__quantidade += qtd
            print(f"Entrada de {qtd}. Estoque: {self.__quantidade}")
        else:
            print("Quantidade inválida!")

    def saida(self, qtd):
        if qtd <= self.__quantidade:
            self.__quantidade -= qtd
            print(f"Saída de {qtd}. Estoque: {self.__quantidade}")
        else:
            print(f"Estoque insuficiente! Disponível: {self.__quantidade}")

    def aplicar_desconto(self, porcentagem):
        if porcentagem >= 1 and porcentagem <= 50:
            self.__preco -= self.__preco * porcentagem / 100
            print(f"Novo preço: R$ {self.__preco:.2f}")
        else:
            print("Desconto deve ser entre 1% e 50%!")

    def valor_em_estoque(self):
        return self.__preco * self.__quantidade

fone = Produto("Fone Bluetooth", 150.0, 10)
caneta = Produto("Caneta", 3.5)

fone.saida(3)
fone.saida(20)
fone.entrada(-5)
fone.aplicar_desconto(80)
fone.aplicar_desconto(10)

caneta.saida(1)
caneta.entrada(100)
caneta.saida(40)
caneta.aplicar_desconto(0)
caneta.aplicar_desconto(20)

print(f"R$ {fone.valor_em_estoque():.2f}")
print(f"R$ {caneta.valor_em_estoque():.2f}")

try:
    fone.quantidade = 1000
except AttributeError:
    print("Não é permitido alterar a quantidade diretamente!")