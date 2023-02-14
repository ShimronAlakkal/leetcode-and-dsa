'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example: 
Input: nums = [1,3,5,6], target = 5
Output: 2

'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums) 


# Test 
test = Solution()
print(test.searchInsert([1,3,5,6],2))

'''
Best solution:

    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        
        return len(nums) # this executes only when the target is greatest than all the elements in nums
'''