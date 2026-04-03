class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # key -> sandwich type [0,1]
        # value -> num of students wanting that type

        sandwich_requests = {
            0: 0,
            1: 0
        }

        for i in range(0, len(students), 1):
            sandwich_requests[students[i]] = sandwich_requests.get(students[i]) + 1

        for i in range(0, len(sandwiches), 1):
            if sandwich_requests.get(sandwiches[i]) <= 0: break

            if sandwich_requests.get(sandwiches[i]) > 0:
                sandwich_requests[sandwiches[i]] -= 1
            else:
                break

        return sum(sandwich_requests.values())