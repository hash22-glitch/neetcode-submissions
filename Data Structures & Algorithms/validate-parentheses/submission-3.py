class Solution:
    def isValid(self, s: str) -> bool:

        dic = {"{":"}", "(":")", "[":"]"}

        stack = []

        for para in s:
            if para in dic:
                stack.append(dic[para])
            else:
                if not stack:
                    return False
                if para != stack[-1]:
                    return False
                stack.pop()
        return len(stack)==0