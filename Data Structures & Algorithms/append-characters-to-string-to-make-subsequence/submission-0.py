class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        seen_chars = 0
        for char in s:
            if seen_chars <= len(t) - 1 and t[seen_chars] == char:
                seen_chars += 1

        if seen_chars == len(t):
            return 0

        return len(t) - seen_chars