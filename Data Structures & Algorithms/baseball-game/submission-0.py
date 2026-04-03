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
                print(final_score)
                final_score += (last_1 + last_2)
                print(final_score)
            elif operation in ["D"]:
                scores.append(scores[len(scores) - 1] * 2)
                print(scores)
                print(final_score)
                final_score += scores[len(scores) - 1]
                print(final_score)
            else:
                score = scores.pop()
                final_score -= score
                print(final_score)

        return final_score