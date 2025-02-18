def twoNumSum(array, targetSum):
    vals = {}
    
    for n in range(len(array)):
        
        val = array[n]
        # print('function called', val)
        x = targetSum - val
        # if val % 2 == 0:
        #     vals[val] = True
        if (array[n] not in vals):
            vals[array[n]] = True
        if (array[n] in vals ) and (x in vals) and x != val:
            print([val, x])
            
    
    print(vals)
    return []



nums = [3,5,-4,8,11,1,-1,6]
target = 10

twoNumSum(nums, target)

# test = {1:True,2:True,3:False,4:False}

# if 3 in test:
#     print('found match')
#     print(test[3])
