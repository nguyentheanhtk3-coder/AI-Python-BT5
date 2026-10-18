a = []
n = int(input())
for i in range(n):
    s = input()
    mang = [int(x) for x in s.split(".")]
    if len(mang) == 4:
        o = "YES"
        for i in mang:
            if type(i) != int :
                o = "NO"
            else:    
                if i >= 0 and i <= 255:
                    continue
                else:
                    o = "NO"   
        a.append(o)                              
    else:
        a.append("NO")
for x in a:
    print(x)