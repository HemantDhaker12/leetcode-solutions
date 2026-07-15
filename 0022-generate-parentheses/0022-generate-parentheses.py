class Solution(object):
    def generateParenthesis(self, n):
        def solve(ind,total,brackets,result):
            if ind>=len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return
            elif total>len(brackets)//2:
                return
            elif total<0:
                return
            brackets[ind]="("
            sum=total+1
            solve(ind+1,sum,brackets,result)
            brackets[ind]=")"
            sum=total-1
            solve(ind+1,sum,brackets,result)
        
        brackets=[""]*(n*2)
        result=[]
        solve(0,0,brackets,result)
        return result

        