# Problem name: Plus One 
# Level: easy
# Problem no: 66

class Solution(object):  # class
    def plusOne(self, digits): # function
        n = len(digits) # length of array
        print('Digits:', digits)
        for i in range(n-1, -1, -1): # {start,end,increment/decrement} 
            
            digits[i] += 1  # increment the digits from last
            print('Increment: ', digits) 
            
            if digits[i] < 10: # when the digit is less the 10
                return digits
            
            digits[i] = 0  # when the no is 10 set the digit as 0 and complete the loop
            
        return [1] + digits  # when the first no is 0 the add [1] in the array[] Eg: [1, ..., array] 

solution = Solution() #creating object
# input values
print(solution.plusOne([1,2,3])) 
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))

