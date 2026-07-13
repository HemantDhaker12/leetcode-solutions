class Solution(object):

    def solve(self,ind,nums,subset):
        if ind >=len(nums):
            self.result.append(subset[:])
            return
        subset.append(nums[ind])
        self.solve(ind+1,nums,subset)
        subset.pop()
        self.solve(ind+1,nums,subset)

    def subsets(self, nums):
        self.result=[]
        self.solve(0,nums,[])

        return self.result
        
         
        