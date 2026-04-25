class Solution:
    def merge(self, arr, s: int, m: int, e: int):
        #[1, 3]    [2, 4]
        l_arr = arr[s:m+1]
        r_arr = arr[m+1:e+1]
        arr_index = s

        l,r = 0,0

        while l <= len(l_arr) - 1  and r <= len(r_arr) - 1:
            if r_arr[r] < l_arr[l]:
                arr[arr_index] = r_arr[r]
                arr_index += 1
                r += 1
            elif l_arr[l] < r_arr[r]:
                arr[arr_index] = l_arr[l]
                arr_index += 1
                l += 1
            else:
                arr[arr_index] = l_arr[l]
                arr_index += 1
                arr[arr_index] = r_arr[r]
                arr_index += 1
                r += 1
                l += 1

        if l <= len(l_arr) - 1:
            while l <= len(l_arr) - 1:
                arr[arr_index] = l_arr[l]
                arr_index += 1
                l += 1

        if r <= len(r_arr) - 1:
            while r <= len(r_arr) - 1:
                arr[arr_index] = r_arr[r]
                arr_index += 1
                r += 1

    def mergeSort(self, arr: List[int], s: int, e: int):
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)
        self.merge(arr, s, m, e)

        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)