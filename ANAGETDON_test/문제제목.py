from itertools import permutations
corrects = []
for A, C, E, N, M, K in permutations([0,1,2,3,4,5,6,7,8,9], 6):
    if A*100 + N*10 + A + C*100 + A*10 + N == M*1000 + A*100 + K*10 + E:
        corrects.append((A + C + E + N + M + K, [A, C, E, N, M, K]))
corrects.sort()
print(*corrects[-1][1])

