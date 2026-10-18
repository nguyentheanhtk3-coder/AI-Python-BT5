n, m = input().split()
n = int(n)
m = int(m)
hang = n
def nto(x):
    so = x
    if so < 2:
        xac_dinh = 0
    else:
        xac_dinh = 1
        for i in range(2, so-1):
            if so % i == 0:
                xac_dinh = 0
                break
    return xac_dinh
mangnto = []
while hang > 0:
    s = input()
    mang = [int(x) for x in s.split()]
    for i in mang:
        ok = nto(i)
        mangnto.append(ok)
    hang -= 1

for i in range(len(mangnto)):
    print(mangnto[i], end=" ")
    if (i + 1) % m == 0:
        print("")    