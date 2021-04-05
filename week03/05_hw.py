a = input().split()
k = int(input())
if abs(k) > len(a):
    if k > 0:
        k = k % len(a)
    else:
        k = -(abs(k) % len(a))
if k >= 0:
    for i in range(len(a) - k, len(a)):
        print(int(a[i]), end = " ")
    for i in range(len(a) - k):
        print(int(a[i]), end = " ")
else:
    for i in range(abs(k), len(a)):
        print(int(a[i]), end = " ")
    for i in range(abs(k)):
        print(int(a[i]), end = " ")