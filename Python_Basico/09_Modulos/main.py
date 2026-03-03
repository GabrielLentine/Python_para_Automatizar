# trazer o código de um arquivo p/ outro utilizando 'import'
import modulos # mas isso só funciona se o outro arquivo estiver no mesmo diretório que o 'main.py'
from funcoes import funcoes_import # esse funciona apenas quando o arquivo está em um diretório diferente do 'main.py'
from modulos import saudacao # importando a função 'saudação' de módulos (que está na raíz, junto de 'main.py')
from funcoes.funcoes_import import saudacao # importando a função 'saudacao' que está no diretório 'Funcoes/funcoes_import.py'
from modulos import * # importando todas (com o *) as funções presentes na raíz do projeto (junto de 'main.py')
from funcoes.funcoes_import import * # importando todas (com o *) as funções presentes em 'Funcoes/funcoes_import'

modulos.saudacao("Gabriel") # import do mesmo diretório de 'main.py'
funcoes_import.saudacao("Mário") # import de diretórios diferente do 'main.py'
saudacao("Henrique") # import direto de 'saudacao' do arquivo 'modulos.py'
saudacao("Lentine") # import direto de 'saudacao' do arquivo 'Funcoes/funcoes_import.py'