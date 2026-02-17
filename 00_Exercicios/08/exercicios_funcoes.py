# funções
# quadrado de um número
def quadrado(numero):
    return pow(numero, 2)

# apresentar uma pessoa
def apresentar_pessoa(nome, idade):
    return f"Nome: {nome} | Idade: {idade} anos"

# par ou ímpar
def verificar_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# chamadas
numero = int(input("Digite um número: "))
numero_quadrado = quadrado(numero)
print(f"{numero} ao quadrado é: {numero_quadrado}")

print(apresentar_pessoa("Gabriel", 19))
print(apresentar_pessoa("Maria", 32))

print(verificar_par(2))
print(verificar_par(3))
