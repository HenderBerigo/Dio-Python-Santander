# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}!")

# idade = input("Digite sua idade: ")
idade = 49
print(idade)
print(type(idade))  # Verificando o tipo da variável idade

idade = int(idade)  # Convertendo a entrada para um número inteiro
print(idade)
print(type(idade))  # Verificando o tipo da variável idade

nome = "Hender"
sobrenome = "Berigo"
# Imprime os valores de nome e sobrenome
print(nome, sobrenome)

print(f"Ola {nome} {sobrenome}, você está com {idade} anos.")
# Imprime os valores separados por " - "
print(nome, sobrenome, idade, sep=" - ")
# Imprime os valores separados por " # "
print(nome, sobrenome, idade, sep="#")  
print(nome, sobrenome, ",", idade, end="\n")
print(nome + sobrenome + ", " + str(idade))
