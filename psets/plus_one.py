'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''


class Solution(object):
    def plusOne(self, digits):
        ns = ''
        for i in digits:
            ns += str(i)
        print(ns)
        
        ns = str(int(ns) + 1)
        s = []
        for i in ns :
            s.append(i)
        
        return s


test = Solution()

print(test.plusOne(['2','4','5','2']))
print(test.plusOne(['9']))

'''
Solution
runtime 16ms
beats blue 83.12%
memory 13.4mb
beats purple 51.78%
'''
