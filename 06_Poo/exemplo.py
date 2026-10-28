#1. Classe: o modelo (planta)

class Celular:
    def __init__ (self, marca, modelo, cor, bateria):
        # Atributos as características do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#4. Métodos: comportamentos do objeto
    def ligar(self):
    # O metodo consulta um atributo do próprio objeto
        if self.bateria == 0:
            print("Sem bateria! Coloque para recarregar!")
        else:
            self.ligado = True
            print("ligado")

    def desligar(self):
        self.ligado = False
        print("Desligado")

#5. Objeto: criados apartir de classe(as casas)
celular1 = Celular("Xiaomi", "Galaxy S25 Ultra", "branco", 54)
celular2 = Celular("Iphone", "18 Pro Max", "Beringela",37)

#6. Acessando e alterando atributos
#usamos objeto.atributo
print(celular1.marca)
print(celular1.modelo)
print(celular2.bateria)

#7. Chamando métodos
#usamos objeto.metodo()
celular2.ligar()
celular2.desligar()


# Atividade

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