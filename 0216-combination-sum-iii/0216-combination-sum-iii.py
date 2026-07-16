class Solution(object):

    def solve(self,last,total,result,subset,k,n):
        if total==n and len(subset)==k:
            result.append(subset[:])
            return
        if total>n or len(subset)>k:
            return
        for i in range(last,10):
            sum=total+i
            subset.append(i)
            self.solve(i+1,sum,result,subset,k,n)
            subset.pop()
        
    def combinationSum3(self, k, n):
        result=[]
        
        self.solve(1,0,result,[],k,n)
        return result
       
        