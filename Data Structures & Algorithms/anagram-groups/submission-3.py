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
                # print(arr_index)
                print(f"arr_index: {arr_index}, value: {str(int(arr[arr_index]) + 1)}")
                arr[arr_index] = str(int(arr[arr_index]) + 1)

            print(arr)
            key = ",".join(arr)
            print(key)

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
            print("\n")

        print(anagrams)
        return list(anagrams.values())
