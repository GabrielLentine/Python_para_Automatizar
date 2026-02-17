# escolha entre pizza, sushi e salada
print('''
    1. Pizza
    2. Sushi
    3. Salada
    ''')

opcao = int(input("Escolha um prato (1 a 3): "))
match opcao:
    case 1:
        print("Você escolheu a pizza")
    case 2:
        print("Você escolheu o sushi")
    case 3:
        print("Você escolheu a salada")
    case _:
        print("Opção inválida!")

# digite um meio de transporte
meio_transporte = input("Digite um meio de transporte: ")
match meio_transporte:
    case 'carro' | 'Carro':
        print("Veículo terrestre")
    case 'bicicleta' | 'Bicicleta':
        print("Transporte sustentável")
    case 'avião' | 'Avião' | 'helicóptero' | 'Helicóptero':
        print("Transporte aéreo")
    case _:
        print("Transporte desconhecido")
