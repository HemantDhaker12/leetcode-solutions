class Solution(object):
    def backtrack(self,index,total,subset,nums,result):
        if total==0:
            result.append(subset[:])
            return
        if total<0:
            return
        if index>=len(nums):
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            sum=total-nums[i]
            self.backtrack(i+1,sum,subset,nums,result)
            subset.pop()

    def combinationSum2(self, candidates, target):
        result=[]
        candidates.sort()
        total=target
        self.backtrack(0,total,[],candidates,result)
        return result
        