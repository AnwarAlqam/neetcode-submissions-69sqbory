class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Apply Gravity
        for row in boxGrid:
            last_free_spot_index = -1
            last_obstacle_index = -1
            last_block_index = -1
            for j in range(len(row) - 1, -1, -1):
                print(f"last_free_spot_index: {last_free_spot_index}")
                print(f"last_obstacle_index: {last_obstacle_index}")
                print(f"j: {j}\n")

                if row[j] == "." and last_free_spot_index == -1:
                    last_free_spot_index = j
                elif row[j] == "*":
                    last_obstacle_index = j
                    last_free_spot_index = -1
                elif row[j] == "#" and last_free_spot_index != -1:
                    row[j] = "."
                    row[last_free_spot_index] = "#"
                    last_free_spot_index -= 1

            print(f"row: {row}\n")

            rows = len(boxGrid)
            cols = len(boxGrid[0])

            # Rotate
            res = []
            for col in range(0, cols, 1):
                rotated = []
                for row in range(rows - 1, -1, -1):
                    rotated.append(boxGrid[row][col])

                res.append(rotated)

        return res