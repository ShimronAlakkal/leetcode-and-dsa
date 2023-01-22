'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

'''
Solution method; Traverse through each letter of the string, check if it is with the others, if it is with the others add it to longestCommonPrefix, else break.
'''

# mysolution
class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		longestCommonPrefix = ""

		for i in range(len(strs)):
			print(i)



		



# test 
test = Solution()
print(test.longestCommonPrefix(["Flower",'Flow',"Fish"]))