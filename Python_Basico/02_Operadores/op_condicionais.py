# if, elif e else
idade = int(input("Qual a sua idade?: "))

if idade >= 18:
    print("Você é maior de idade")
elif idade <= 17 and idade >= 15:
    print("Você é um adolescente")
else: # idade <= 14
    print("Você é menor de idade")

senha = "batatinha"
tentativa_senha = input("Digite a sua senha: ")

if tentativa_senha == senha:
    print("Senha correta! Pode entrar!")
if tentativa_senha != senha:
    print("Senha incorreta! Você não pode entrar!")
