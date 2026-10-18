def doicoso(x, y):
    so = ""
    while x > 0:
        m = x % y
        if m < 10:
            so += str(m)
        else:
            so += chr(m + 55)
        x = x // y
    return so

n = int(input())
mang = []
while n > 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == "":
        break

    so = doicoso(a, b)
    mang.append(so[::-1])
    n -= 1

for x in mang:
    print(x)