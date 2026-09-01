class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rp=[]
        for s in tokens:
            if s =="+":
                rp.append(rp.pop()+rp.pop())
            elif s=="-":
                a,b=rp.pop(),rp.pop()
                rp.append(b-a)
            elif s=="*":
                rp.append(rp.pop()*rp.pop())
            elif s=="/":
                a,b=rp.pop(),rp.pop()
                rp.append((int(b/a)))
            else:
                rp.append(int(s))
        return rp[0]