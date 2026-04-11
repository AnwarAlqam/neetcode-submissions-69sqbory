class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen_chars = 0
        for char in t:
            if seen_chars <= len(s) - 1 and char == s[seen_chars]:
                seen_chars += 1

        if seen_chars == len(s):
            return True

        return False