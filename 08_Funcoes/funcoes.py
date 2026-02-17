# utiliza-se o nome reservado 'def'

# funções
def helloWorld():
    print("Olá, Mundo!")

def saudacao(nome):
    print(f"Olá, {nome}. Seja bem-vindo!")

def somar(num_1, num_2):
    resultado = num_1 + num_2
    print(f"{num_1} + {num_2} = {resultado}")

# chamadas
helloWorld() # função sem argumentos
saudacao("Gabriel") # função com um argumento
somar(1, 2) # função com dois argumentos
