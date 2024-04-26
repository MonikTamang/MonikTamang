# Problem name: Largest Number At Least Twice of Others
# Level: easy
# Problem no: 747
class Solution(object):
    def dominantIndex(self, nums):
        length = len(nums)  # length of array
        greatest = nums[0]  # default greatest number
        status = 1 # Current Status
       
        # find greatest number
        for i in range(0, length-1):
            if greatest < nums[i+1]:
                greatest = nums[i+1]
       
        # find if greatest number is at least equal to twice other numbers
        for i in range(0, length):
            # do not check with the greatest number
            if greatest == nums[i]:
                pass
            # check condition
            elif nums[i] * 2 > greatest:
                status = -1 # if greater than greatest number
        if status == 1:
           return nums.index(greatest) # return index of greatest
        else:
            return status # return -1


solution = Solution()
#input values
print(solution.dominantIndex(nums = [3, 6, 1, 0]))
print(solution.dominantIndex(nums = [1, 2, 3, 4]))