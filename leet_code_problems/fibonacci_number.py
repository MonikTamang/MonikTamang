# Problem name: Fibonacci Number
# Level: Easy
# Problem no: 509

class Solution(object):
    def fib(self, n):
        a = 0 
        b = 1
        
        if n == 0:
            return a # for num = 0 
        
        if n == 1:
            return b # for num = 1 
        
        if n > 1: # for num greater than 1
            for i in range(2, n+1):
                
                temp = a + b # create a temporary variable to store sum
                a = b # replace value of one step ahead
                b = temp   
                                           
        return temp # return the last sum value

# input values
solution = Solution()
print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(4))