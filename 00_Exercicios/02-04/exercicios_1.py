# Exercícios das aulas abaixo

# Exercício 1: Calcule a soma da sequência 10 ao 14
soma = sum([10, 11, 12, 13, 14])
print(soma)

# Exercício 2: Calcule a média entre os número 10, 15 e 20
numeros = [10, 15, 20]
media = sum(numeros) / len(numeros)
print(media)

# Exercício 3: Usuário digita duas notas (de 0 a 10) e o peso de cada uma
# Calcule a média ponderada entre elas
# Exemplo: media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
# Obs: a soma dos pesos precisa ser 10
nota1 = input("Digite a primeira nota: ")
nota1 = eval(nota1) # tudo que passa dentro dela, ela trata como um int

peso1 = input("Qual o peso dessa nota?: ")
peso1 = eval(peso1) # tudo que passa dentro dela, ela trata como um int

nota2 = input("Digite a segunda nota: ")
nota2 = eval(nota2) # tudo que passa dentro dela, ela trata como um int

peso2 = input("Qual o peso dessa nota?: ")
peso2 = eval(peso2) # tudo que passa dentro dela, ela trata como um int

mediaPonderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print(mediaPonderada)

pesoNotas = peso1 + peso2
print(pesoNotas)

# Exercício 4: Qual o menor preço da lista: 100.20, 34.90, 31.50, 18.95
menorPreco = min([100.20, 34.90, 31.50, 18.95])
print(menorPreco)

# Exercício 5: Verifique se o menor preço é menor que 20.00
if menorPreco < 20.00:
    print("É menor que 20")
else:
    print("É maior que 20")

# Exercício 6: Número digitado é par ou ímpar
num = input("Digite um valor: ")
num = eval(num)

if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")
