def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    if(s[0] == s[-1]):
        return isPalindrome(s[1:-1])
    else:
        return False

s: str = input().lower()
clear_s = [i for i in s if i.isalpha() or i.isdigit()]

print(isPalindrome(clear_s))
    