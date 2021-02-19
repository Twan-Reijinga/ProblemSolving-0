s = int(input())
m = 0
for i in range(5)[::-1]:
  m += s // (i+1)
  s = s % (i+1)
print(m)