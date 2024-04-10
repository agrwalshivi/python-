def binary_search(arr, a, low, high):
    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == a:
            return mid

        elif arr[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
a = 4
#printing the array
print("The given array is", arr)

#printing element to be found
print("Element to be found is ", a)

index = binary_search(arr, a, 0, len(arr)-1)

if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
