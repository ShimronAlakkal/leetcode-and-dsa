'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 == 0:
            return ( nums[l/2] + nums[ (l/2) - 1 ] ) / 2.0
        return nums[l//2]



test = Solution()
print(test.findMedianSortedArrays([1,2],[3,4]))
print(test.findMedianSortedArrays([1],[2]))