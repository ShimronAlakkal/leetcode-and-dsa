'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

'''


# my solution
class Solution:
	def isValid(self, s: str) -> bool:
		length = len(s)
		if length >= 1 and length <= 10**4:
			for i in s:
				if i not in '(){}[]':
					return False
				
				# The code for the else part
				pass
					
		return False;


# test 
test = Solution()
print(test.isValid('()[]{}'))

# Best solutions















