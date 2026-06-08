import sys
input = sys.stdin.readline
found = False
s = 1
e = 1000000001
mid = (e-s) // 2
while not found:
    print(f"? {mid}")
    sys.stdout.flush()
    answer = input().strip()
    if answer == '+':
        s = mid
        mid = (e+s) // 2
        continue
    elif answer == '-':
        e = mid
        mid = (e+s) // 2
        continue
    else:
        print(f"! {mid}")
        found = True
        break 