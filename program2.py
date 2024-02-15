class Solution(object):
  def romanToInt(self,s: str) -> int:
    r_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_result = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and r_int[s[i]] < r_int[s[i+1]]:
            final_result -= r_int[s[i]]
        else:
            final_result += r_int[s[i]]
    
    return final_result

obj=Solution()

# print(obj.romanToInt("III"))       
print(obj.romanToInt("LVIII"))     
print(obj.romanToInt("MCMXCIV"))   
