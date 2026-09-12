class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n, in enumerate(nums):
            goal = target-n
            if goal in hm:
                return [hm[goal], i]
            hm[n] = i