# exercício 1
import random as rd

# exercício 1
while True:
    numero_sorteado = rd.randint(1, 10)
    tentativas = 0

    while numero_sorteado:
        op = int(input("Digite um chute: "))
        if op > numero_sorteado:
            print("Muito alto!")
            tentativas += 1
        elif op < numero_sorteado:
            print("Muito baixo!")
            tentativas += 1
        else:
            print("Acertou!")
            tentativas += 1
            break

    print(f"Foram necessários {tentativas} tentativas até acertar!")
    break
