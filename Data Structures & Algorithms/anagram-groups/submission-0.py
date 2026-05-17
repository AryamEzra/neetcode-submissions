class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = set()
        dic = defaultdict(list)
        ans = []
        l = len(strs)
        for i in range(l):
            cur = strs[i]
            word = sorted(cur)
            word = "".join(word)
            dic[word].append(cur)

        for k,v in dic.items():
            ans.append(v)
        return ans
        