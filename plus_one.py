class Solution(object):  # class
    def plusOne(self, digits): # function
        n = len(digits) # length of array
        print('Digits:', digits)
        for i in range(n-1, -1, -1): # {start,end,increment/decrement} 
            
            digits[i] += 1  # increment the digits from last
            print('Increment: ', digits) 
            
            if digits[i] < 10: # when the digit is less the 10
                return digits
            
            digits[i] = 0  # when the no if 10 set the digit as 0 and complete the loop
            print('carry: ', digits)
            print('When 9: ', [1] + digits ) 
        return [1] + digits  # when the first no is 0 the add [1] in the array[] Eg: [1, ..., array] 

solution = Solution() #creating object
print(solution.plusOne([1,2,3])) #call and print the function output
print(solution.plusOne([9]))
print(solution.plusOne([1,9,9]))
print(solution.plusOne([1,7,9]))