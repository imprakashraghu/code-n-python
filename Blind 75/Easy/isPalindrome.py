#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

def isAlphaNum(c):
  if ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or
     (ord(c) >= ord('a') and ord(c) <= ord('z')) or
     (ord(c) >= ord('0') and ord(c) <= ord('9'))):
       return True
  else:
    return False
  
def isPalindrome(s):
  # TODO: O(n)
  # Two Pointer Algorithm
  left , right = 0, len(s) - 1
  while left < right:
    while left < right and not isAlphaNum(s[left]):
      left += 1
    while left < right and not isAlphaNum(s[right]):
      right -= 1
    if s[left].lower() != s[right].lower():
      return False
    left += 1
    right -= 1
  return True