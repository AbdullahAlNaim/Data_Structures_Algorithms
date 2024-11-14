
def removeElement(nums, val):
    k = 0
    for x in range(len(nums)):
        if nums[x] != val:
            nums[k] = nums[x]
            k += 1
        if nums[x] == val:
            continue
    print(k)
    return k
one = [3,2,2,3]
vOne = 3

two = [0,1,2,2,3,0,4,2]
vTwo = 2
removeElement(two, vTwo)