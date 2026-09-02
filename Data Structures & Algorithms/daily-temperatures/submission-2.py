class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        s=[]
        for i,t in enumerate(temperatures):
            while s and t >s[-1][0]:
                st,si=s.pop()
                answer[si]=(i-si)
            s.append([t,i])
        return answer  
        
        