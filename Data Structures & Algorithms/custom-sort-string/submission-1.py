class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        unneeded_sort = []
        needed_sort = []

        char_order = defaultdict(int)
        for char in order:
            char_order[char] = len(char_order) + 1

        for char in s:
            if char not in char_order:
                unneeded_sort.append(char)
            else:
                needed_sort.append(char)

        sorted_items = sorted(needed_sort, key=lambda x: char_order[x])

        return "".join(sorted_items) + "".join(unneeded_sort)
