from datetime import datetime

agora = datetime.now()
print(agora) # data atual
print(agora.day) # dia atual
print(agora.month) # mês atual
print(agora.year) # ano atual
print(agora.hour) # hora atual
print(agora.minute) # minuto atual
print(agora.second) # segundo atual
print(agora.microsecond) # milissegundos atuais
print(agora.strftime("Hoje é dia %d do mês %m do ano ano %Y")) # %d - dia | %m - mês | %Y - ano (cheio) | %y ano (dois últimos dígitos)
print(agora.strftime("Agora são %H horas e %M minutos")) # %H - horas | %M - minutos

aniversario = datetime(2006, 8, 1, 10, 10, 00) # criando uma data (yyyy-mm-dd)
print(aniversario)

data_str = "20/04/2026"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y") # srtptime() converte uma string em uma data
print(data_convertida)
