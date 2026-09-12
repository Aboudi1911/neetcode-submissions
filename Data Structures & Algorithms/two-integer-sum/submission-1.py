class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal = (target-nums[i])
            for j in range (len(nums)):
                if nums[j] == goal and j != i:
                    ls = [j, i]
        return ls