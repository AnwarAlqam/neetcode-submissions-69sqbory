class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        
        top_left = [0, 0]
        top_right = [0, cols - 1]
        bottom_left = [rows - 1, 0]
        bottom_right = [rows - 1, cols - 1]

        res = []

        print(f"top_left: {top_left}")
        print(f"top_right: {top_right}")
        print(f"bottom_left: {bottom_left}")
        print(f"bottom_right: {bottom_right}")

        while top_left[1] < top_right[1]:
            # take top row
            for col in range(top_left[1], top_right[1], 1):
                res.append(matrix[top_left[0]][col])

            # take right column
            for row in range(top_right[0], bottom_right[0], 1):
                res.append(matrix[row][top_right[1]])

            # take bottom row
            for col in range(bottom_right[1], bottom_left[1], -1):
                res.append(matrix[bottom_right[0]][col])

            # take left column
            for row in range(bottom_left[0], top_left[0], -1):
                res.append(matrix[row][bottom_left[1]])

            # Reduce indexes by 1 (going to inner square/rectangle)
            top_left = [top_left[0] + 1, top_left[1] + 1]
            top_right = [top_right[0] + 1, top_right[1] - 1]
            bottom_left = [bottom_left[0] - 1, bottom_left[1] + 1]
            bottom_right = [bottom_right[0] - 1, bottom_right[1] - 1]

        # Take center number if there and not in res
        if top_left[0] == top_right[0] and top_left[0] == bottom_left[0]:
            res.append(matrix[top_left[0]][top_left[1]])

        return res