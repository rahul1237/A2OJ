import math
def disb2p(x1,y1,x2,y2):
    return (math.sqrt((x2-x1)**2+(y2-y1)**2))

a,x1,y1,x2,y2=map(int,input().split())
print(math.ceil(disb2p(x1,y1,x2,y2)/(2*a)))
# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan