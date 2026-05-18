class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        

        s = set()
        hm = {i : [] for i in range(n)}
        
        for i in edges:
            hm[i[0]].append(i[1])
            hm[i[1]].append(i[0])
        
        def dfs(node, parent):
            if node in s:
                return False
            s.add(node)
            for i in hm[node]:
                if i == parent:
                    continue
                else:
                    dfs(i, node)
        
        dfs(0, -1)
        return len(s) == n










