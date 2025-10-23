n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    l1=[]
    while(i!=0):
        rem=i%10
        l1.append(rem)
        i//=10
    s+=min(l1)
    l1=0
print(s)

