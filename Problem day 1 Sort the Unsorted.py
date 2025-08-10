n= int(input())
if n>=1 and n<=10**5:
    
    
    arr=list(map(int, input().split()))
    if len(arr)==n:
        for i in range(n):
            if arr[i]<-10**9 or arr[i]>10**9:
               exit()
        arr.sort()
        print(*arr)