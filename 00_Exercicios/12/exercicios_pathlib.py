from pathlib import Path

# exercício 1
# pasta_dados = Path("Dados/Entrada/Saida")
# pasta_dados.mkdir(parents=True, exist_ok=True)

# pasta_relatorios = Path("Relatorios")
# pasta_relatorios.mkdir(exist_ok=True)

# exercício 2
arquivo_entrada1 = Path(r"E:\PYTHON\Python_Basico_Aulas\00_Exercicios\12\Dados\Entrada/dados.txt")
arquivo_entrada2 = Path(r"E:\PYTHON\Python_Basico_Aulas\00_Exercicios\12\Dados\Entrada/dados2.txt")
arquivo_entrada3 = Path(r"E:\PYTHON\Python_Basico_Aulas\00_Exercicios\12\Dados\Entrada/dados3.txt")
arquivo_entrada1.touch()
arquivo_entrada2.touch()
arquivo_entrada3.touch()

# exercício 3
iterar_pasta = Path(r"E:\PYTHON\Python_Basico_Aulas\00_Exercicios\12\Dados\Entrada")
for arq in iterar_pasta.glob("*.txt"):
    print(arq)
