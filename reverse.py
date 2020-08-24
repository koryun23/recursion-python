def reverse(arr,first):
    if len(arr) == first:
        return
    print(arr[-1])
    [arr[-1]].append(reverse(arr[:-1],first))
    



reverse([1,2,3,4],0)
# reverse([1,2,3,4],1)
# reverse([1,2,3,4],2)
# reverse([1,2,3,4],3)


