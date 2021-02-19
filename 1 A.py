s = input("")
a = s.count("a")
geenA = len(s) - a
for i in range(geenA):
  if a <= geenA:
    geenA -= 1
print(a + geenA)
