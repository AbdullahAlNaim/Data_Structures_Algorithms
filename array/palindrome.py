def isPalindrome(s: str) -> bool:
        newS = [c.lower() for c in s if c.isalnum()]
        newS = ''.join(newS)
        
        print(newS == newS[::-1])
        return newS == newS[::-1]


isPalindrome("A man, a plan, a canal: Panama")