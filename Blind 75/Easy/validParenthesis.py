#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#s = "()}{[(])"
def _isValid(s):
  if len(s) <= 1:
    return False
  stack = []
  for i in s:
    if (len(stack) > 0 and (i == ')' and stack[-1] == '(') or
       (len(stack) > 0 and i == ']' and stack[-1] == '[') or
       (len(stack) > 0 and i == '}' and stack[-1] == '{')):
         stack.pop()
    else:
      stack.append(i)
  return len(stack) == 0


def isValid(s):
    Map = { ")":"(", "]":"[", "}":"{" }
    stack = []
    
    for c in s:
        if c not in Map:
            stack.append(c)
            continue    
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()
        
    return False