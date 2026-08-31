class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open={")":"(", "}":"{","]":"["}
        for i in s:
            if i in open:
                if stack and stack[-1] == open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        