a, b, c = map(int, input().split())

maiorNum = (a+b+abs(a-b))/2
if maiorNum > c:
  print(maiorNum,'eh o maior')
else:
  print(c,'eh o maior')


