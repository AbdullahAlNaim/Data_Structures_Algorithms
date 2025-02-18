# def searchInsert(nums, target):
#     hash = {}
#     for x in range(len(nums)):
#         if nums[x] == target:
#             print('match found ' + str(x))
#             return x
#         elif nums[x] != target and nums[x] < target:
#             continue
#         elif nums[x] != target and nums[x] > target:
#             print('match found ' + str(x))
#             return x

def searchInsert(nums, target):
    l, r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            print(mid)
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else: 
            r = mid - 1

    print(l)
    return l
        
nums = [1,3,5,6]

targetOne = 5 # answer is 2
targetTwo = 2 # answer is 1
targetThree = 7 # answer is 4

searchInsert(nums, targetTwo)