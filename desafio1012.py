A, B, C = map(float, input().split())
PI = 3.14159
tri = '{:.3f}'.format((A*C)/2)
cir = '{:.3f}'.format(PI*C**2)
tra = '{:.3f}'.format(((A+B)*C)/2)
qua = '{:.3f}'.format(B*B)
ret = '{:.3f}'.format(A*B)

print('TRIANGULO:', tri)
print('CIRCULO:', cir)
print('TRAPEZIO:', tra)
print('QUADRADO:', qua)
print('RETANGULO:', ret)


