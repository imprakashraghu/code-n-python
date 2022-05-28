#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Input: s = "anagram", t = "nagaram"
#Output: true

#Brute Force Sol
def _isAnagram(s, t):
  # TODO: O(n log n)
  s = ''.join(sorted(s)) # O(n log n)
  t = ''.join(sorted(t)) # O(n log n)
  return s==t # 1

def isAnagram(s, t):
  # TODO: O(n) S(n)
  # Frequency Counter Pattern
  if len(s) != len(t): # 1
    return False
  countOfS = {}
  countOfT = {}
  for i in s: # n
    if i in countOfS:
      countOfS[i] += 1
    else:
      countOfS[i] = 1
  for j in t: # n
    if j in countOfT:
      countOfT[j] += 1
    else:
      countOfT[j] = 1
  for x in countOfS: # n
    if countOfT.get(x, 0) != countOfS[x]:
      return False
  return True
