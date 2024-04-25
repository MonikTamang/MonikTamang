# Problem name: Ugly Number
# Level: Easy
# Problem no: 263

class Solution(object): # class
    def isUgly(self, n): # function
        if n == 0: # check if number is 0 or not
            return False # return fase if not ugly number
        
        for i in [2, 3, 5]: # select value of i from list [ 2, 3, 5 ]
            while n % i == 0: # while the number is divisible by i
            # prime numbers like 7, 11 etc are not divisible by 2, 3 and 5 so it will the num value will not be 1 
                n /= i # change the value of the number by diving it with value of i
        
        return n == 1  # the number will be 1 when it is divisible by 2, 3 and 5

solution = Solution()  # create object to call the function

#required input values
print(solution.isUgly(6)) 
print(solution.isUgly(1))
print(solution.isUgly(14))