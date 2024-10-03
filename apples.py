class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = set()

        def _dfs(curr_node):
            if curr_node in visited:
                return 0

            visited.add(curr_node)
            total_sum = 0
            for node in adj_list[curr_node]:
                total_sum += _dfs(node)

            if total_sum > 0 or hasApple[curr_node]:
                return total_sum + 2
            return total_sum

        res = _dfs(0)
        return res-2 if res else res
        