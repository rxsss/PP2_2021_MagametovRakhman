a = input().split()
for i in range(len(a)):
    if a[i] != "0":
        print(int(a[i]), end = " ")
for i in range(len(a)):
    if a[i] == "0":
        print(int(a[i]), end = " ")