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

n = input()
m = input()
mang = [int(x) for x in m.split()]
mang.sort()
for i in range(len(mang)):
    for j in range(i, len(mang)):
        a = nto(mang[i])
        b = nto(mang[j])
        if mang[i] != 0:
            if mang[j] % mang[i] == 1 or ((a == 1 or b == 1) and mang[j] % mang[i] != 0) or mang[i] == 1:
                print(mang[i], mang[j])