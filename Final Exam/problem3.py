'''
Determine if a string is a palindrome (reads the same forwards and backwards)
DO NOT use reverse() or aString[:,:,-1] in Python
'''
def isPalindrome(s):
    '''
    s is a String
    '''
    length=len(s)
    i = 0
    while i < length//2 :
        i += 1
        if s[i] !=s[length-i-1]:
            return False;
    return True;

# Test case:
# s = 'abcba'
# palindrome = isPalindrome(s)  
