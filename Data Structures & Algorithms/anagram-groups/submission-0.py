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
            summation_value = 0
            for char in word:
                summation_value += ord(char)
            if summation_value not in anagrams:
                anagrams[summation_value] = []
            anagrams[summation_value].append(word)

        return list(anagrams.values())
