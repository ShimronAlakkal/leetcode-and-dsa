'''
Given an integer x, return true if x is a palindrome, and false otherwise.


Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''


'''
Runtime : 56 ms
Beats: 91.14% in runtime
Memory : 13.8 Mb
Beats : 96.5% in memory
'''

# my solution
class Solution:
	def isPalindrome(self, x: int) -> bool:
		sx = str(x)
		length = len(sx)
		return sx[0 : length // 2 : 1] == sx[length - 1 : length // 2 - 1 : -1] if not(length % 2) else sx[0 : length // 2 : 1] == sx[length - 1 : length // 2 : -1]


	
# test 
test = Solution()
print(test.isPalindrome(181))


# Best Solution 
'''
# Runtime : 30 ms
# memory : 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x==x[::-1]:
            return True
        return False   
'''