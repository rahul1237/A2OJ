a=int(input())
b=list(map(int,input().split()))
for _ in range(1,a):
    if b[_-1]>b[_]:
        if(sorted(b)==b[_:]+b[:_]):
            print(a-_)
        else:
            print(-1)
        break
else:
    print(0)

# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan