# Listas, Tuplas e Dicionários

# 1. Listas

# Listas são utilizadas para armazenar vários valores
# dentro de uma única variável

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

# 2. Acessando elementos da lista

print(nomes[0])
print(nomes[1])

# Podemos acessar o último elemento usando -1

print(nomes[-1])

# 3. Alterando elementos

# As listas são mutáveis, ou seja, os elementos podem ser alterados

nomes[0] = "Pedro"
print(nomes)

# 4. Adicionando elementos

# append() adiciona um elemento no final da lista

nomes.append("Lucas")
print(nomes)

# insert() adiciona um elemento em uma posição

nomes.insert(1, "Mariana")
print(nomes)

# 5. Removendo elementos

# remove() remove um elemento pelo seu valor

nomes.remove("Lucas")
print(nomes)

# pop() remove um elemento pelo índice

nomes.pop(0)
print(nomes)

# 6.Tamanho a lista

# len() informa a quantidade e elementos.

print(len(nomes))

# 7. Percorrendo ma lista

for nome in nomes:
    print(nome)

# 8. Verificando se um elemento existe

if "João" in nomes:
    print("João está na lista")
else:
    print("João não está a lista")

# 9. Lista com diferentes tipos de dados

dados = ["João", 18, 1.75, True]

# 10. Lista e números

notas = [7.5, 8.0, 6.5, 9.0]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.1f}")

# 11. Tuplas
# Tuplas são semelhantes a listas
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas

coordenadas = (10, 20)
print(coordenadas)

# Acessando elementos.
print(coordenadas[0])
print(coordenadas[1])

# 12. Dicionários
# Dicionarios armazenam informações no formato:
# chave: valor

aluno = {

    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}
print(aluno)

# 13. Acessando valores do dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# 14. Alterando valores

aluno["nota"] = 9.0
print(aluno)
