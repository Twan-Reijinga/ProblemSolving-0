n = int(input())
p = input().split()
s = 0
for i in range(len(p)):
    s += int(p[i])
print(f"{s/n:.12f}")