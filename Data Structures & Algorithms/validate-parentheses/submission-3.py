class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ')' and (stack.pop() != '('):
                    return False
                elif s[i] == '}' and (stack.pop() != '{'):
                    return False
                elif s[i] == ']' and (stack.pop() != '['):
                    return False
        return not stack