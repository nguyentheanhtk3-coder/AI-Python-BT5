def tong_chiadoi(x):
    s = str(x)
    lenx = len(s)
    nua = lenx // 2
    a = int(s[:nua])
    b = int(s[nua:lenx])
    tong = a + b
    return tong

n = int(input())
while n > 9:
    n = tong_chiadoi(n)
    print(n)