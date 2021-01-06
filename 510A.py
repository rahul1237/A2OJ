a,b=map(int,input().split())
for _ in range(a):
    if(_%2!=0):
        if(_%4>=2):
            print('#'+('.'*(b-1)))
        else:
            print(('.'*(b-1))+'#')
    else:
        print('#'*b)


# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan