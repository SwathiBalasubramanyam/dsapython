class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_swaps = 0

        while True:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                num_swaps = 0
            else:
                students = students[1:] + [students[0]]
                num_swaps += 1

            if num_swaps == len(students):
                break

            if not students:
                break

        return len(students)



