class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        nums.sort()
        if n==1:
            return nums[0]
        
        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            if count==floor(n//2):
                return nums[i]
         
                


        