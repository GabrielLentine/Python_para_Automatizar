# global
import sys # p/ fechar o sistema assim que o usuário teclar '6'

# listas globais p/ utilizações futuras
info_alunos = []
notas = []

# funções
def main_menu():
    # menu principal
    print("""
        1. Adicionar Aluno
        2. Listar Todos os Alunos
        3. Buscar Aluno Pelo Nome
        4. Remover Aluno
        5. Mostrar Média Geral das Notas
        6. Sair
    """)

    op = int(input("Digite um valor: "))
    match op:
        case 1:
            adicionar_alunos()
            main_menu()
        case 2:
            listar_alunos()
            main_menu()
        case 3:
            busca_aluno_nome()
            main_menu()
        case 4:
            remover_aluno()
            main_menu()
        case 5:
            notas_aluno()
            main_menu()
        case 6:
            sys.exit()

def adicionar_alunos():
    # simples: pede vários dados e acrescenta na lista global
    print("---------- ADICIONAR ALUNO ----------")
    aluno = {
        "nome": input("Nome do Aluno: "),
        "idade": input("Idade do Aluno: "),
        "matricula": int(input("Nº da Matrícula: ")),
    }
    info_alunos.append(aluno)

    print("Aluno adicionado com sucesso!")
    print("-----------------------------------")

def listar_alunos():
    # simples: se não tiver alunos, a mensagem aparece. Se tiver, vai percorrer toda a lista e ir listando os alunos)
    print("---------- LISTAR ALUNOS ----------")
    if len(info_alunos) == 0:
        print("Sem alunos cadastrados!")

    for alunos in info_alunos:
        print(alunos)
    print("-----------------------------------")

def busca_aluno_nome():
    # simples: vai buscar o nome na lista e mostrar o aluno
    print("---------- BUSCAR ALUNO PELO NOME ----------")
    nome_aluno = input("Digite o nome do aluno: ")

    for aluno in info_alunos:
        if aluno.get("nome") == nome_aluno: # aluno recebe a instância de info_alunos, por isso é possível utilizar o .get() p/ buscar o nome
            print(f"Aluno encontrado: {aluno}")
        else: "Aluno não encontrado!"
    print("-----------------------------------")

def remover_aluno():
    # simples: vai buscar o nome na lista e remover o aluno
    print("---------- REMOVER ALUNO ----------")
    nome_aluno = input("Digite o nome do aluno: ")

    for aluno in info_alunos:
        if aluno.get("nome") == nome_aluno: # aluno recebe a instância de info_alunos, por isso é possível utilizar o .get() p/ buscar o nome
            info_alunos.remove(aluno)
            print("Aluno removido com sucesso!")
        else: "Aluno não encontrado!"
    print("-----------------------------------")

def notas_aluno():
    print("---------- MÉDIA DAS NOTAS DO ALUNO ----------")
    nome_aluno = input("Digite o nome do aluno: ")

    for aluno in info_alunos:
        if aluno.get("nome") == nome_aluno: # aluno recebe a instância de info_alunos, por isso é possível utilizar o .get() p/ buscar o nome
            incrementador = 0 # vai garantir que todas as notas sejam digitadas
            cont = int(input("Quantidade de notas: "))

            while incrementador != cont: # isso é a garantia (enquanto incrementador e cont não forem iguais, as notas serão passadas)
                nota = float(input("Digite a nota: "))
                notas.append(nota)
                incrementador += 1 # sempre somando com o resultado anterior p/ garantir que o loop encerre

            resultado = media_notas(notas) # método responsável pelo cálculo da média
            print(f"A média do aluno {aluno} é {resultado}")
        else: "Aluno não encontrado!"
    print("-----------------------------------")

def media_notas(notas):
    media = 0

    for n in notas:
        media += n
    return round(media / len(notas), 1)
    # vai retornar a soma das notas divididos pela quantidade de notas presentes na lista
    # o round() garante que a nota não terá muitas casas decimais, apenas uma (ex: 9,1666 => 9,2)

# chamadas
main_menu()
