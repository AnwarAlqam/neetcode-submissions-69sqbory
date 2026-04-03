class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        final_score = 0
        for operation in operations:
            if operation not in ["+", "D", "C"]: # Add new score
                scores.append(int(operation))
                final_score += int(operation)
            elif operation in ["+"]:
                last_1 = scores[len(scores) - 1]
                last_2 = scores[len(scores) - 2]
                scores.append(last_1 + last_2)
                final_score += (last_1 + last_2)
            elif operation in ["D"]:
                scores.append(scores[len(scores) - 1] * 2)
                final_score += scores[len(scores) - 1]
            else:
                score = scores.pop()
                final_score -= score

        return final_score