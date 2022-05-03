import math

valor = int(input())

cont100 = math.floor(valor/100) #notas de 100
resto1 = valor%100 #resto
cont50 = math.floor(resto1/50) #notas de 50
resto2 = resto1%50 #resto
cont20 = math.floor(resto2/20) #notas de 20
resto3 = resto2%20 #resto
cont10 = math.floor(resto3/10) #notas de 10
resto4 = resto3%10
cont5 = math.floor(resto4/5) #notas de 5
resto5 = resto4%5
cont2 = math.floor(resto5/2) #notas de 2
resto6 = resto5%2
cont1 = math.floor(resto6/1) #notas de 1

print(valor)
print(cont100, 'nota(s) de R$ 100,00')
print(cont50, 'nota(s) de R$ 50,00')
print(cont20, 'nota(s) de R$ 20,00')
print(cont10, 'nota(s) de R$ 10,00')
print(cont5, 'nota(s) de R$ 5,00')
print(cont2, 'nota(s) de R$ 2,00')
print(cont1, 'nota(s) de R$ 1,00')

