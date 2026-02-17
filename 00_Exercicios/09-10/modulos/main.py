# exercício 1
from funcoes.matematica import *
from funcoes.mensagens import *

# exercício 2
from meu_pacote.formatador import *
from meu_pacote.numeros import *

# exercício 3
from perfil.usuario import *
from perfil.validacao import *

# exercício 1
nome = input("Digite o seu nome: ")
num = int(input("Digite um número: "))

boas_vindas(nome)
print(dobro(num))
print(metade(num))

# exercício 2
texto = input("Digite uma frase ou texto: ")
print(caixa_alta(texto))

numero = int(input("Digite um número: "))
print(eh_par(numero))

# exercício 3
nome_usuario = input("Digite o nome de usuário: ")
idade_usuario = int(input("Digite a idade do usuário: "))
print(idade_valida(idade_usuario))

perfil_usuario = criar_perfil(nome_usuario, idade_usuario)
print(perfil_usuario)
