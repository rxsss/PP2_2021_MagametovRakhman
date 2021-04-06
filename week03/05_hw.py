a = input().split()
k = int(input())
<<<<<<< HEAD
if k >= 0:
    for i in range(k):
        a[i] = a[len(a) + i -k]
    for i in range(len(a) - 1, k-1, -1):
        a[i] = a[i-k]
print(a)
=======
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
>>>>>>> bc84f1439b076bc96d8873efc131ba5317674cd7
