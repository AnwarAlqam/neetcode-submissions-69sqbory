class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a = 1
        # b = 2
        # c = 3
        # ...
        # act
        # 1 3 7

        anagrams = {} # key: summation, value: array of words
        for word in strs:
            key = ""
            arr = ["0"] * 26

            for char in word:
                arr_index = ord(char) - ord('a')
                arr[arr_index] = str(int(arr[arr_index]) + 1)
            key = "".join(arr)
            
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())
