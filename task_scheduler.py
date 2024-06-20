class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = defaultdict(int)
        for task in tasks:
            task_cnt[task] += 1

        # time = 0
        # seq = []
        # for k, v in task_cnt.items():
        #     new_seq = []
        #     for _ in range(v):
        #         new_seq += ["_"] * time + [k] + ["_"] * (n-time)
        #     seq.append(new_seq)
        #     time += 1

        # merged_list = []
        # from itertools import zip_longest
        # for values in list(zip_longest(*seq, fillvalue='_')):
        #     picked_val = False
        #     for value in values:
        #         if value != '_':
        #             merged_list.append(value)
        #             picked_val = True
        #             break
        #     if not picked_val:
        #         merged_list.append('_')
        
        # while merged_list and merged_list[-1] == "_":
        #     merged_list.pop()
        # return len(merged_list)

        seq = []
        more_tasks = True
        while more_tasks:
            more_tasks = False
            total_tasks_per_cycle = 0
            for k,v in task_cnt.items():
                if v <= 0:
                    continue
                more_tasks = True
                seq.append(task)
                total_tasks_per_cycle += 1
                task_cnt[k] -= 1

            if any(x > 0 for x in task_cnt.values()) and total_tasks_per_cycle <= n:
                seq += ["idle"] * (n+1-total_tasks_per_cycle)
        return len(seq)
            

from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies of each task
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        # Step 2: Create a max heap based on task frequencies
        max_heap = [-cnt for cnt in task_count.values()]
        heapq.heapify(max_heap)

        # Step 3: Initialize variables for time tracking
        time = 0
        cooldown = deque()

        # Step 4: Process tasks using the max heap and cooldown queue
        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Take the most frequent task
                if count != 0:
                    cooldown.append((count, time + n))  # Append to cooldown with release time

            if cooldown and cooldown[0][1] == time:  # Check if a task can be released from cooldown
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time


Solution().leastInterval(["A","C","A","B","D","B"], 1)