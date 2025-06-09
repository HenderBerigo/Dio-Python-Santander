# numeros = [1, 30, 21, 2, 9, 65, 34, 71, 84, 17, 22, 68, 44]
# pares = []
# impares = []

# FILTRAR ITENS DA LISTA 01
# for numero in numeros:
#   if numero % 2 == 0:
#     pares.append(numero)
#   else:
#     impares.append(numero)
    
# print("Ímpares")
# print(impares)
# print("Pares")
# print(pares)

# FILTRAR ITENS DA LISTA 02
# pares = [numero for numero in numeros if numero % 2 == 0]
# impares = [numero for numero in numeros if numero % 2 != 0]

# print("Ímpares")
# print(impares)
# print("Pares")
# print(pares)

# # MODIFICANDO VALORES
# quadrado = [numero ** 2 for numero in numeros]
# print("Ao quadrado")
# print(quadrado)

# #SOMANDO
# soma = 0
# for numero in numeros:
#   soma += numero
# print(soma)
#         # 1,  2,  3,  4,  5,  6
# lista = ["p","y","t","h","o","n"]

# print(lista[2:]) # t, h, o, n
# print(lista[:2]) # p, y
# print(lista[1:3]) # y, t
# print(lista[:3:2]) # p, t
# print(lista[:]) # p, y, t, h, o, n  
# print(lista[::]) # p, y, t, h, o, n  
# print(lista[::-1]) # n, o, h, t, y, p
# print(lista[2::2]) # t, o
# print(lista[1::3]) # y, n
# print(lista[::5]) # p, n
# print(len(lista))

# for item in lista: # EXIBIR ITENS DA LISTA
#   print("Letra:", item)

# for indice, item in enumerate(lista): #ENUMERATE
#   print(f"{indice}: {item}")

# frutas = ["laranja", "maça", "uva"]
# print(frutas)

# frutas = []
# print(frutas)

# letras = list("python")
# print(letras)

# numeros = list(range(10))
# print(numeros)

# carro = ["Ferrari", "F8", 420000, 2020, 2900, "Osasco-SP", True]
# print(carro)

# frutas = ["laranja", "maça", "uva"]
# print(frutas[-1])
# print(frutas[-3])

# matriz = [
#   [1, "a", 2],
#   ["b", 3, 4],
#   [6, 5, "c"]
# ]

# print(matriz[0])
# print(matriz[0][0])
# print(matriz[0][-1])
# print(matriz[-1][-1])

#         # 1,  2,  3,  4,  5,  6
# lista = ["p","y","t","h","o","n"]
# lista_maiuscula = []

# # Passando por cada item da lista
# for item in lista:
# # adicionando cada item da lista em nova lista com item em maiúsculo
#   lista_maiuscula.append(item.upper())
  
# print(lista_maiuscula)


# # APPEND
# lista_geral = []
# lista_geral.append(1)
# lista_geral.append("Teste")
# lista_geral.append(True)
# lista_geral.append(10.12)
# lista_geral.append(["Hender", 49, "SP"])

# # print(lista_geral)

# # COPY - Faz a cópia sem alterar a original
# lista_geral_2 = lista_geral.copy()
# lista_geral_2.append("SIM")
# print(lista_geral)
# print(lista_geral_2)

# CLEAR

# lista_geral.clear()
# print(lista_geral)

lista = ["p","y","t","h","o","n"]
# lista.pop()
# print(lista)

# lista_2 = ["p","y","t","h","o","n"]
lista_2 = lista[::-1].copy()
lista_2.pop()
lista.pop()

print(lista_2)
print(lista)


