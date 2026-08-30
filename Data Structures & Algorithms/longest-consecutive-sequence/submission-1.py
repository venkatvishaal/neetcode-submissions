class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums) # store array in a set to check for left neighbour of an element
        long=0 # initialize the length of the longest subsequence to 0
        for i in nums:
            if (i-1) not in numset: # check if the element value -1 is in the set ie(e=100, check if 99 is present in set , if not proceed as it is the starting value)
                length=0
                while(i+length) in numset: # checking for each consecutive number in the set 
                    length+=1
                long=max(length,long)
        return long        