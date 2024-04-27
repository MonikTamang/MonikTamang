# Problem name: keep multiplying found values by two
# Level: easy
# Problem no: 2154

class Solution(object):
    def findFinalValue(self, nums, original):
     
        while (original in nums):
            original *= 2

        return original
       
       
solution = Solution()
print(solution.findFinalValue(nums = [5, 3, 6, 1, 12], original = 3))
print(solution.findFinalValue(nums = [2, 7, 9], original = 4))