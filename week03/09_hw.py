n = input().split()
anya = []
borya = []
for i in range(int(n[0])):
    a = int(input())
    anya.append(a)
for i in range(int(n[1])):
    a = int(input())
    borya.append(a)
print(len(set(anya) & set(borya)))
print(*sorted(set(anya) & set(borya), key=int))
print(len(set(anya) - set(borya)))
print(*sorted((set(anya) - set(borya)), key=int))
print(len(set(borya) - set(anya)))
print(*sorted(set(borya) - set(anya), key=int))