import math

seg = int(input())

horas = math.floor(seg/3600)
resto1 = seg%3600
minutos = math.floor(resto1/60)
segundos = resto1%60

print(str(horas)+":"+str(minutos)+":"+str(segundos))
