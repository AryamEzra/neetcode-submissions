class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for s in strs:
            val = [0] * 26
            for c in s:
                val[ord(c) - 97] += 1
            
            graph[tuple(val)].append(s)
        # print(graph)
        ans = []
        for k,v in graph.items():
            ans.append(v)
        return ans

        
        
        