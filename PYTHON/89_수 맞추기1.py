s = 1
while 1:
    print("?",s)
    answer = input()
    if answer == "NO":
        s += 1
    else:
        print("!",s)
        break