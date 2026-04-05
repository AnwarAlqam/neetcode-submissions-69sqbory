class Solution:
    def __init__(self): 
        self.reminder = {}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        if n == 2:
            return 2

        if n in self.reminder:
            return self.reminder[n]

        self.reminder[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.reminder[n]
