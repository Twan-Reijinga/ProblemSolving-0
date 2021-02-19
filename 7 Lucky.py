n = input()
if len(n)==4 or len(n)==7:
    c = 0
    for d in n:
        if d=="4" or d=="7":
            c += 1
    if len(n)==c:
        print("YES")
    else:
        print("NO")
else: 
    print("NO")