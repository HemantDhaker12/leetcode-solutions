class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        i=0
        j=0
        if n==1:
            return 1
        
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
