from collections import defaultdict 

def groupAnagram(strs: list[str]) -> list[list[str]]:
    anagram = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram[key].append(word)

    print(list(anagram.values()))
    return list(anagram.values())

groupAnagram(['eat', 'ate', 'tea', 'tan', 'nat', 'bat'])
