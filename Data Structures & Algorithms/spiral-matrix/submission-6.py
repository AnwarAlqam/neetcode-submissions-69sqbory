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

        while top_left[0] <= bottom_left[0] and top_left[1] <= top_right[1]:
            # take top row (left → right, INCLUSIVE)
            for col in range(top_left[1], top_right[1] + 1):
                res.append(matrix[top_left[0]][col])

            # take right column (top → bottom, skip first)
            for row in range(top_right[0] + 1, bottom_right[0] + 1):
                res.append(matrix[row][top_right[1]])

            # Only take bottom row if we have more than one row
            if top_left[0] < bottom_left[0]:
                # take bottom row (right → left, skip first)
                for col in range(bottom_right[1] - 1, bottom_left[1] - 1, -1):
                    res.append(matrix[bottom_right[0]][col])

            # Only take left column if we have more than one column
            if top_left[1] < top_right[1]:
                # take left column (bottom → top, skip first and last)
                for row in range(bottom_left[0] - 1, top_left[0], -1):
                    res.append(matrix[row][bottom_left[1]])

            # Reduce indexes by 1 (going to inner square/rectangle)
            top_left = [top_left[0] + 1, top_left[1] + 1]
            top_right = [top_right[0] + 1, top_right[1] - 1]
            bottom_left = [bottom_left[0] - 1, bottom_left[1] + 1]
            bottom_right = [bottom_right[0] - 1, bottom_right[1] - 1]

        return res