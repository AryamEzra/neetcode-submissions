class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        graph = dict(Counter(nums))
        heap = []

        for key,v in graph.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [item[1] for item in heap]