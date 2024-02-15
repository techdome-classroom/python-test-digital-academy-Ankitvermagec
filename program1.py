class Solution(object):
  def isValid(self,s: str) -> bool:
    arr = []
    b_ = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in b_.values():
            arr.append(char)
        elif char in b_.keys():
            if not arr or arr.pop() != b_[char]:
                return False
        else:
            
            return False

    
    return not arr

obj=Solution()

# print(obj.isValid("()"))      
# print(obj.isValid("()[]{}"))   
      


  

