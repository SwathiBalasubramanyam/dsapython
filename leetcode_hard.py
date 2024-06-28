# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    from collections import deque

    # time complexity --> o(m*n*k)
    # space complexity --> o(m*n*k)

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1,0), (0, 1), (-1, 0), (0,-1))

        def _inbound(r, c):
            row_inbound = 0 <= r < ROWS
            col_inbound = 0 <= c < COLS
            return row_inbound and col_inbound

        # row, col, steps, eliminations_remaining
        queue = deque([(0,0,0,k)])
        visited = set((0,0, k))

        while queue:
            row, col, steps, elims_remaining = queue.popleft()

            if row == ROWS-1 and col == COLS-1:
                return steps

            for dr, dc in DIRS:
                new_row = row + dr
                new_col = col + dc

                if (new_row, new_col, elims_remaining) in visited:
                    continue

                if not _inbound(new_row, new_col):
                    continue

                if grid[new_row][new_col] == 1 and not elims_remaining:
                    continue

                queue.append((new_row, new_col, steps+1, elims_remaining if grid[new_row][new_col] == 0 else elims_remaining-1))
                visited.add((new_row, new_col, elims_remaining))

        return -1
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                L1 = lists[i]
                L2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.mergeList(L1, L2))

            lists = mergedLists
        return lists[0]

    def mergeList(self, L1, L2):
        dummy = ListNode()
        tail = dummy

        while L1 and L2:
            if L1.val <= L2.val:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next
            tail = tail.next

        if L1:
            tail.next = L1
        if L2:
            tail.next = L2
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        resNode = ListNode()
        resTail = resNode
        org_k = k

        while head:
            dummyNode = ListNode()
            tail = dummyNode
            while head and k:
                tail.next = head
                head = head.next
                tail = tail.next
                tail.next = None
                k -= 1

            if not k:
                resTail.next = self.reverseLinkedList(dummyNode.next)
                k = org_k
                for i in range(k-1):
                    resTail = resTail.next
            else:
                resTail.next = dummyNode.next
            resTail = resTail.next

        return resNode.next

    def reverseLinkedList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
