a,b=map(int, input().split())
for _ in sorted(list(map(int, input().split())) for _ in range(b)):
    if _[0]<a:
        a+=_[1]
    else:
        print('NO')
        exit()
print("YES")
# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan