# linear search
def LinearSearch(arr,tar):
    for i in range (len(arr)):
        if arr[i]==tar:
            return i 
        else:
            return -1

#binary search 
def binary_search(arr,tar):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            right = mid - 1
        else:
            left = mid + 1
    return -1

#recursive binary search

def binarySearch(arr, low, high, x):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1

# Two pointers approach for searching sum of two indeces
def TwoPointerSearch(arr,tar):
    " array must be sorted "
    left=0
    right=len(arr)-1
    while left<=right:
        CurrSum = arr[left]+arr[right]
        if CurrSum==tar:
            return (left,right)
        elif CurrSum > tar:
            right -= 1
        else:
            left += 1
    
    return -1
        
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    tar = 50
    
    # Function call
    # result = LinearSearch(arr,tar)
    # result = binary_search(arr,tar)
    # result = binarySearch(arr,0,len(arr)-1,tar)
    result = TwoPointerSearch(arr,tar)
    
    if result != -1:
        print("target is present at index", result)
    else:
        print("target is not present in array")
