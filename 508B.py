def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

a=input()
la=a[-1]
eve=[]
ans=0
nil=0
for _ in a:
    if(int(_)%2==0):
        eve.append(_)

if(len(eve)==0):
    print(-1)
else:
    for _ in range(len(a)):

        if(int(a[_])%2==0):
            nil=_
            if(int(a[_])<int(la)):
                c=swapPositions(list(a),_,-1)
                ans=1
                break
                    # c=swapPositions()
    if(ans==0):
        c=swapPositions(list(a),nil,-1)
    print(''.join(c))
# while(int(la)>int(a[st]%2==0)):

# CodeBy: RAHUL MAHAJAN
# A2OJ: rahulmahajan
# CC: anonymous0201
# CF: rahulmahajan
# CSES: rahulmahajan