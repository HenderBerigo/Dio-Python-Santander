preco = 10
print(type(preco))
print(preco)
# Convertendo tipos de dados
preco = float(preco)
print(type(preco))
print(preco)

preco = str(preco)
print(type(preco))
print(preco)

preco = 10 /2
print(f"{preco:.2f}")

preco = 10 // 3
print(preco)

print("***************")
preco = "29,90"
print(type(preco))
print(preco)
print("Convertendo string para float")
preco = float(preco.replace(",", "."))
print(type(preco))
print(preco)

print("Convertendo float para string")
preco = str(preco)
print(type(preco))
print(preco)

print("Convertendo float para string formatada")
# print(f"R$ {float(preco):.2f}".replace('.', ','))
preco = f"R$ {float(preco):.2f}".replace('.', ',')
print(type(preco))
print(preco)
