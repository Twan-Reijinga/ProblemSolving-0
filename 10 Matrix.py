for x in range(5):
    i = input().find("1")
    if i != -1:
        print(int(abs(i/2 - 2) + abs(x - 2)))
