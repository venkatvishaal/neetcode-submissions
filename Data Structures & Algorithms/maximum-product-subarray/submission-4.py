class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) # may be the largest if nums has only one element
        currMax,currMin=1,1
        for n in nums:
            tmp=currMax*n
            currMax=max(currMax*n,currMin*n,n)
            currMin=min(tmp,n*currMin,n)
            res=max(res,currMax)
        return res
        