'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321

'''

class Solution(object):
    def reverse(self, x):
        x, v = str(x), 0
        if x[0] == '-':
            v = -int(x[-1:-len(x):-1])
        else:
            v = int(x[-1::-1])
        
        if -2**31 < v < 2**31 - 1:
            return v 
        return 0
