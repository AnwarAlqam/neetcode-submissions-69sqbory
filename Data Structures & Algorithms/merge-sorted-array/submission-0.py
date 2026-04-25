class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l_arr = nums1[0:m]
        r_arr = nums2
        l,r = 0,0
        arr_index = 0

        while l <= m - 1  and r <= n - 1:
            if r_arr[r] < l_arr[l]:
                nums1[arr_index] = r_arr[r]
                arr_index += 1
                r += 1
            elif l_arr[l] < r_arr[r]:
                nums1[arr_index] = l_arr[l]
                arr_index += 1
                l += 1
            else:
                nums1[arr_index] = l_arr[l]
                arr_index += 1
                nums1[arr_index] = r_arr[r]
                arr_index += 1
                r += 1
                l += 1

        if l <= m - 1:
            while l <= m - 1:
                nums1[arr_index] = l_arr[l]
                arr_index += 1
                l += 1

        if r <= n - 1:
            while r <= n - 1:
                nums1[arr_index] = r_arr[r]
                arr_index += 1
                r += 1