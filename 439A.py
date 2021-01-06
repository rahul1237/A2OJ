a,b=map(int,input().split())
c=list(map(int,input().split()))
d=(sum(c)+10*(a-1))
if(d<=b):
    print((b-d)//5+(a-1)*2)
else:
    print(-1)

# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan