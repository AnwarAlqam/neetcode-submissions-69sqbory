class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        char_delete = False

        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end] and char_delete == True:
                return False

            if s[start] != s[end] and char_delete == False:
                char_delete = True
            
            start += 1
            end -= 1

        return True