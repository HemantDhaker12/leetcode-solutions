class Solution(object):

    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset[:])
            return 
        elif total>target:
            return
        if index>=len(nums):
            return
        sum=total+nums[index]
        subset.append(nums[index])
        self.solve(index,sum,subset,nums,target,result)
        sum=total
        subset.pop()
        self.solve(index+1,sum,subset,nums,target,result)
    def combinationSum(self, candidates, target):
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result
        

        


        
        