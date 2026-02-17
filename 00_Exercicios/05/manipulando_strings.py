# primeira e última letra
palavra = input("Digite uma palavra: ")
print(f"A primeira letra da palavra '{palavra}' é '{palavra[0]}'.")
print(f"A última letra da palavra '{palavra}' é '{palavra[-1]}'.")

# fatiamento de frase
frase = input("Digite uma frase: ")
num_1 = int(input("Digite o primeiro número p/ fatiamento: "))
num_2 = int(input("Digite o segundo número p/ fatiamento: "))
print(frase[num_1:num_2])

# arrumando uma frase
frase_arrumar = "    @prendendo @ progr@m@r   "
frase_arrumada = frase_arrumar.strip().replace("@", "a").capitalize()
print(frase_arrumada)
