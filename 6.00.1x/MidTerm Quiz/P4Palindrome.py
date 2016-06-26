def isPalindrome(aString):
    return aString == '' or aString[0] == aString[-1] and isPalindrome(aString[1:-1])