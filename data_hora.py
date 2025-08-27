# Importa o módulo datetime
from datetime import datetime, date, time, timedelta

# 1. Pegar a data e hora atual
agora = datetime.now()
print("Data e hora atual:", agora)

# 2. Pegar só a data
hoje = date.today()
print("Data de hoje:", hoje)

# 3. Criar uma data específica
data_especifica = date(2025, 8, 27)  # Ano, mês, dia
print("Data específica:", data_especifica)

# 4. Criar um horário específico
horario = time(14, 30, 0)  # Hora, minuto, segundo
print("Horário específico:", horario)

# 5. Formatar datas como string
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)

# 6. Converter string para datetime
data_str = "27/08/2025 19:30:00"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("Data convertida:", data_convertida)

# 7. Operações com datas
amanha = hoje + timedelta(days=1)
print("Amanhã:", amanha)

ontem = hoje - timedelta(days=1)
print("Ontem:", ontem)
