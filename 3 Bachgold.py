n = int(input())
if n % 2 == 0:
  k = int(n/2)
  print(k)
  print("2 "*k)
else:
  k = int(n/2 - 1.5)
  print(k+1)
  print("2 "*k + "3")