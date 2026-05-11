S = input()
if S[0] == 'b' and S[-1] == 'a':
    for i in range(1, len(S)-1, 2):
        if S[i] == 'a' and S[i+1] == 'n':
            continue
        print("bananakick")
        exit()
    print("banana")
else:
    print("bananakick")