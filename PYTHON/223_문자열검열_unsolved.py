from collections import deque
result = deque()

S = input()
T = input()


def eq_str():
    pass
# 스택에 넣고 나올 때마다 그 부분 pop하기. 라고 생각함.
for i in range(len(T)):
    result.append(S[i])

for i in range(len(T), len(S)):
    result.append(S[i])

    