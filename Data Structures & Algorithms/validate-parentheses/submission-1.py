class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for ch in s:
            # Closing logic
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            # Opening logic
            else:
                stack.append(ch)
        
        return True if not stack else False