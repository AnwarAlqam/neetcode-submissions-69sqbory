class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        seen_chars = 0
        s_index = 0
        for char in t:
            if char == s[s_index]:
                s_index += 1
                seen_chars += 1

        if seen_chars == len(s):
            return True

        print(seen_chars)

        return False