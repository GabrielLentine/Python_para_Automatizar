# 10 a 1
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

# 5 números digitados e somados
numeros = []
for n in range(1, 6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

resultado = 0
for n in numeros:
    resultado += n
print(resultado)

# digitando valores p/ compor um cofrinho
valores = []
cont = 1

while cont != 0:
    numero = int(input("Digite o valor (em reais): "))
    valores.append(numero)
    cont = numero

resultado = 0
for v in valores:
    resultado += v
print(resultado)

# votação
print("""
    1. Pizza
    2. Hambúrger
    3. Sair
""")
votacao = []
pizza = []
hamburger = []
cont = 1

while cont != 3 and cont == 1 or cont == 2:
    valor = int(input("Escolha entre 1 e 2 (aperte 3 p/ sair): "))

    if valor == 1:
        votacao.append(valor)
        pizza.append(valor)
    elif valor == 2:
        votacao.append(valor)
        hamburger.append(valor)
    cont = valor

resultado = 0
for v in votacao:
    resultado += v
print(f"Foram comptuados {len(pizza)} para Pizza e {len(hamburger)} para hambúrgeres")