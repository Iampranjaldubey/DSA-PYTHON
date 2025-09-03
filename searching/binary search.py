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