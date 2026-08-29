class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        count=[[] for i in range(len(nums)+1)]
        for n in nums:
            res[n]=1+res.get(n,0)
        for n, c in res.items():
            count[c].append(n)
        resl=[]
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                resl.append(n)
                if len(resl)==k:
                    return resl

        