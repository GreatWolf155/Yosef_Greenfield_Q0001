"""
16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers
at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

nums = [-1,2,1,-4]
target = 1
# because of the constraints
closest_to_target = sum(nums[0:3])

for index1 in range(0, len(nums)):
    for index2 in range(index1 + 1, len(nums)):
        for index3 in range(index2 + 1, len(nums)):
            if abs((nums[index1] + nums[index2] + nums[index3]) - target) < abs(closest_to_target - target):
                closest_to_target = nums[index1] + nums[index2] + nums[index3]
print(closest_to_target)