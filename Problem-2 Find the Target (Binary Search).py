def binarysearch (arr, target):
    
    lower=0
    upper = len(arr)-1
    
    while lower<= upper:
        
        mid=(lower+upper)//2
        
        if arr[mid]==  target:
            
            return mid #returns the index of the target value if we find it
        else :
            if arr[mid] < target:\
                
                   lower=mid+1
                    
            else:
                
                upper= mid-1
                
    return -1
                
                
                   
    
    
n= int(input()) #the size of the list

arr= list(map(int, input().split())) #the array elements

target = int(input())

print(binarysearch(arr,target))
