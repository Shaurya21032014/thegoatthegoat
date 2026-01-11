def binary__search(arr, target):
    left=0
    right=len(arr)-1
    steps=0


    while left<=right:
        steps+=1
        mid=(left+right)//2



        print(f"Step {steps}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid]==target:
            print("found the number")
            print("total steps:", steps)
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1


    print("number not found")
    return -1



# Example usage:
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
binary__search(numbers, 15)