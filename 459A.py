a,b,c,d=map(int,input().split())
if(a==c):
    print(a+abs(b-d),b,c+abs(b-d),d)
elif(b==d):
    print(a,b+abs(a-c),c,d+abs(a-c))
elif(abs(a-c)!=abs(b-d)):
    print(-1)
else:
    print(a,d,c,b)




# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan