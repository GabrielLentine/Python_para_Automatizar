# nota mínima (6)
nota = int(input("Digite a nota do seu teste: "))

if nota > 6:
    print("Sua pontuação foi acima da média!")
elif nota == 6:
    print("Sua pontuação foi a nota mínima!")
else:
    print("Sua pontuação está abaixo da média!")

# nomes iguais ou diferentes
primeiro_nome = input("Digite o primeiro nome: ")
segundo_nome = input("Digite o segundo nome: ")

if primeiro_nome == segundo_nome:
    print("Os nomes são iguais!")
else:
    print("Os nomes são diferentes!")


# elegibilidade mínima
idade = int(input("Digite a sua idade: "))

if idade >= 15:
    print("Você pode participar do evento!")
else:
    print("Você não pode participar do evento!")
