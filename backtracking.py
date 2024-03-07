# https://leetcode.com/problems/all-paths-from-source-to-target/description/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from copy import copy
        
        results = []
        def _backtrack(node, path):
            if node == len(graph) - 1:
                results.append(path.copy())
                return

            for pathNode in graph[node]:
                path.append(pathNode)
                _backtrack(pathNode, path)
                path.pop()

        _backtrack(0, [0])
        return results
        
        