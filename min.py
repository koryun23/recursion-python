def min(arr):
    if len(arr) == 1:
        return arr[0]
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    if min(arr1) < min(arr2):
        return min(arr1)
    else:
        return min(arr2)

print(min([1,2,3,4]))
print(min([8,4,9,3]))
print(min([0,7,-5,9]))