class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] # empty list to store the stack values
        open={")":"(", "}":"{","]":"["} # hashmap to check for open brackets and close bracket mathcing
        for i in s: # for every character in the string
            if i in open: # if that character is in the hashmap
                if stack and stack[-1] == open[i]: # checks if the stack is empty and the top of the stack is equal to the character ie (close ==open)
                    stack.pop()  #pop that pair 
                else:
                    return False
            else:
                stack.append(i) # if not closing bracket push inside the stack 
        return True if not stack else False

        