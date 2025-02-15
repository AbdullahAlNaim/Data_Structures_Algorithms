def isValidSubSequence(array, sequence):
    s, a = 0, 0
    while s < len(sequence) and a < len(array):
        if sequence[s] == array[a] and s == len(sequence) - 1:
            print(True)
            return True
        elif sequence[s] == array[a]:
            s += 1
            a += 1
        elif sequence[s] != array[a]:
            a += 1
    print(False)
    return False

# arr = [5,1,22,25,6,-1,8,10]
arr = [5, 1, 22, 25, 6, -1, 8, 10]
# seq = [1,6,-1,10]
seq = [4, 5, 1, 22, 25, 6, -1, 8, 10]

isValidSubSequence(arr, seq)