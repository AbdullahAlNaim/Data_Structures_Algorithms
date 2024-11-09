test = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

# first attempt
def twoNumberSum(array, targetSum):
    one = 0
    two = 0
    for x in range(len(array)):
        one = array[x]
        two = targetSum - one
        # print(one, two)
        for y in range(len(array)):
            if array[y] == two and array[y] != array[x]:
                print(one, two)
                return [one, two]
            else:
                continue

# second attempt
def hashing(array, targetSum):
    hasher = {}
    for x in range(len(array)):
        one = array[x]
        two = targetSum - one
        if hasher[array[x]] == true and hasher[two] == true:
            [array[x], two]
            return [array[x], two]

# first answer
def summer(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                print([firstNum, secondNum])
                return [firstNum, secondNum]
    return []

        
# second answer
def twoNumHash(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True

    return []


# third solution
def twoNumPoint(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            print([array[left], array[right]])
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
        

# twoNumberSum(test, target)
# hashing(test, target)

# solution O(n^2) time | O(1) space
summer(test, target)

# solution O(n) time | O(n) space
twoNumberSum(test,target)

# solution O(nlog(n)) time | O(1) space
twoNumPoint(test, target)