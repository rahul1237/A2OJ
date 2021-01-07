a,b=map(int,input().split())
c=list(map(int,input().split()))
d,e=0,0
ans=0
for i in range(1,a+1):
    d+=c[i-1]
    if d>b:
        d-=c[e]
        e+=1
print(a-e)

# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan