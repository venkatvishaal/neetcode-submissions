class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s)) + "#" + s  # For the encoding of the string we first count the number of characters in the string and keep in the first postion ie 0th position , then we keep a delimiter character and encode the string.
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        # for decoding first we set the i pointer(what postion we are at input string) to be inbounded and then we initialize the j pointer to the ith index and we search for the delimilter if it is not found we increment it. the length of the string will be starting from index i to j but not including them. Length says how many following we have to read after j th index. j+1 is the first character after delimiter and we have to go till the length (j+1+length) and append it to the list.

        while i < len(s):
            j=i # first postion is at an integer
            while s[j] != "#":
                j+=1
            length= int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res

