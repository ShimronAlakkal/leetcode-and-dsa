'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Solution: Return a list of indeces of the elements in the nums list that add up to target.
Runtime: 4249 ms
Best Solution Runtime: 87 ms
'''

# my solution
class Solution:

	def twoSum(self, nums : list[int], target : int) -> list[int]:
		
		indexList = []

		for i in range(0,len(nums)):
			for j in range(i + 1, len(nums)):

				if nums[i] + nums[j] == target:
					indexList.append(i)
					indexList.append(j)
		return indexList




# test run 
'''
nums = [3,4,5,2,5]
target = 5

'''

test = Solution()
print(test.twoSum([3,2, 4],6))


# # best solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = dict()
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i

