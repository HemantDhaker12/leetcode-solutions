class Solution(object):
    def solve(self,index,subset,result,digits):
        if index>=len(digits):
            result.append("".join(subset))
            return
        for ch in self.char_map[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,result,digits)
            subset.pop()
    def letterCombinations(self, digits):
         self.char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

         result=[]
         self.solve(0,[],result,digits)
         return result
        