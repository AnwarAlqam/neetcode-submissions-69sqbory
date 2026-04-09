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

        common_prefixes = [key for key, value in prefixes.items() 
                          if value == len(strs)]
        
        if not common_prefixes:
            return ""
        
        # Return the longest common prefix
        return max(common_prefixes, key=len)