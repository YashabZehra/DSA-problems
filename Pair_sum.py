arr = [1, 2, 3, 4, 6]
target = 6

def pair_sum(arr,target):
    left , right = 0 , len(arr)-1

    while left<right:
        current_sum = arr[left]+arr[right]

        if current_sum == target:
            return[left,right]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return []
    
print(pair_sum([1,2,3,4,6],6)) #output: [1,3] = 2+4 = 6
            
