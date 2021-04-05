class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cntr = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        cntr += 1
        return cntr
first = Solution()
first.numIdenticalPairs([1,2,3,1,1,3])
# print("i = " + str(i) + " " + str(nums.index(i)))