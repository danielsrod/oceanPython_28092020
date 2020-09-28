from datetime import datetime

agora = datetime.now()

diaatual = agora.day
mesatual = agora.month
anoatual = agora.year

hora = agora.hour
minu = agora.minute

print(f"{diaatual:02}/{mesatual:02}/{anoatual:04}")
print(f"{hora:02}:{minu:02}")