a,b=map(int,input().split())
c=list(map(int,input().split()))
ea=[]
ans=0
for _ in c:
    if(_<0):
        ea.append(_)
# print(ea)
if(len(ea)<=b):
    print(sum(ea)*-1)
else:
    ea=sorted(ea)
    for _ in range(b):
        ans+=ea[_]
    print(ans*-1)

# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan