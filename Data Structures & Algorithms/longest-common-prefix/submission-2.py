class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefixes = {}

        for word in strs:
            prefix = ""
            for char in word:
                prefix += char
                prefixes[prefix] = prefixes.get(prefix, 0) + 1

        if len(prefixes) == 0:
            return ""

        max_value = max(prefixes.values())

        if max_value <= 1:
            return ""

        max_keys = [key for key, value in prefixes.items() if value == max_value]

        return max(max_keys, key=len)