from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listMap = {}
        for i, n in enumerate(nums):
            if target - n in listMap:
                return [listMap[target - n], i]
            listMap[n] = i

Sol = Solution()
nums = [2,7,11,15]
print(Sol.twoSum(nums, target=9))
