class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = {}

        for n in nums:
            if n not in topk:
                topk[n] = 0
            topk[n] += 1

        desc = {key: value for key, value in sorted(
            topk.items(), key=lambda item: item[1], reverse=True
        )}

        klist = []
        for key in list(desc)[:k]:
            klist.append(key)

        return klist