class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t): return False
      letter_s = {}
      letter_t = {}

      for i in range(len(s)):
         letter_s[s[i]] = letter_s.get(s[i], 0) + 1
         letter_t[t[i]] = letter_t.get(t[i], 0) + 1


      return letter_s == letter_t

    

solution = Solution()
        
s = "racecar"
t = "carrace"


print(solution.isAnagram(s, t))
