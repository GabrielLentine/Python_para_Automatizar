# mostrar os valores contidos em um dicionário de livros
from turtle import clear


livros = {
    "título": "Memórias Póstumas de Brás Cubas",
    "autor": "Machado de Assis",
    "editora": "Martin Claret",
    "ano": "2021"
}

print(livros["título"])
print(livros["autor"])
print(livros["editora"])
print(livros["ano"])

print()

# verificar uma idade de um dicionário
nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))
usuario = {
    "nome": nome,
    "idade": idade
}

if usuario["idade"] >= 18:
    print(f"Acesso liberado para {usuario['nome']}!")
else:
    print(f"Acesso negado para {usuario['nome']}!")

print()

# sistema de login com dois dicionários
nome_cadastro = input("Digite seu nome para se cadastrar: ")
senha_cadastro = input("Digite sua senha para se cadastrar: ")

cadastro = {
    "nomeCadastro": nome_cadastro,
    "senhaCadastro": senha_cadastro
}

if cadastro:
    print("Cadastro realizado com sucesso!")
else:
    print("Não foi possível realizar o seu cadastro!")

print()

nome_verificar = input("Digite o seu nome para logar: ")
senha_verificar = input("Digite sua senha para logar: ")

verificacao = {
    "nomeVerificar": nome_verificar,
    "senhaVerificar": senha_verificar
}

if verificacao["nomeVerificar"] == cadastro["nomeCadastro"] and verificacao["senhaVerificar"] == cadastro["senhaCadastro"]:
    print("Login bem-sucedido!")
else:
    print("Credenciais inválidas!")