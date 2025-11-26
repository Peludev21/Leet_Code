class Solution:
    @staticmethod
    def twosum(nums, target):
        long = len(nums)
        for i in range(long):
            for j in range(i + 1, long):
                if nums[i] + nums[j] == target:
                    return [i,j]




solution =  Solution()
nums = [9,5,2,7,3,5,2,1,6,7,4,2]
print(solution.twosum(nums, 5))
