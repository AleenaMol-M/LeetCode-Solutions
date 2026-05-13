# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Array, HashMap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=[]
        i=0
        while(i<n):
            for j in range(i+1,n):
              if( nums[i]+nums[j]==target):
                 l.append(i)
                 l.append(j)
                 return l
                 
            i=i+1
