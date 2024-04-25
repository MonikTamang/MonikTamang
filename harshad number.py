# Problem name: harshad number
# Level: easy
# Problem no: 3099

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):                 
        y = x
        sum = 0  
        while(y > 0):
            sum += (y % 10)     # add remainders to find the digits sum
            y //= 10    # quotient

        if x % sum == 0:  # check number is divisible by sum
            return sum # if yes return print the number
        else:
            return -1 # else return -1

solution = Solution()
#input
print(solution.sumOfTheDigitsOfHarshadNumber(18))
print(solution.sumOfTheDigitsOfHarshadNumber(23))