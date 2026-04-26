class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"#{len(s)}{s}#"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i <= len(s) - 1:
            if s[i] == "#" and i + 1 <= len(s) - 1 and s[i + 1].isdigit():
                j = i + 1
                length_str = ""
                while j < n and s[j].isdigit():
                    length_str += s[j]
                    
                    j += 1

                if length_str == "":
                    i += 1
                    continue
                length = int(length_str)
                start = j
                end = start + length
                res.append(s[start:end])
                i = end + 1  # skip trailing '#'
        return res