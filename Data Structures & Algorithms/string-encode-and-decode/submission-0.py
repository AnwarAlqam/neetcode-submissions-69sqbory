class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"#{len(s)}{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i <= len(s) - 1:
            if s[i] == "#" and i + 1 <= len(s) - 1 and s[i + 1].isdigit():
                char_len = int(s[i + 1])
                res.append(s[i+2:i+2+char_len])
                i = i + 2 + char_len
        return res