def sortedSquaredArray(array):
    # Write your code here.
    sortedSqrs = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSqrs[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSqrs[idx] = largerValue ** 2
            largerValueIdx -= 1

    return sortedSqrs