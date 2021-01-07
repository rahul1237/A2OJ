a=input()
b=int(input())
c=list(map(int,input().split()))
d=0
for _ in range(len(a)):
    d+=c[ord(a[_])-97]*(_+1)
print(d+max(c)*(b*(b+1)//2+len(a)*b))


# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan