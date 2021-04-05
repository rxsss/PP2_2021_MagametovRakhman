a = input().split()
b = []
for i in range(len(a)):
    if int(a[i]) > 0:
        b.append(int(a[i]))
print(min(b))