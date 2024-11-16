def singleNum(nums):
    hash = {}
    for x in range(len(nums)):
        if nums[x] not in hash:
                hash[nums[x]] = False
        else:
            hash[nums[x]] = True

    # print(ans.keys())
    key = next((k for k, v in hash.items() if v == False), None)
    print(key)
    
singleNum([2,2,1])