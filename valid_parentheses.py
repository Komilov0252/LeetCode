def isValid( s: str) -> bool:
    hashmap = {'(':')', '{':'}', '[':']'}
    stack = []
    for char in s:
        if char in hashmap:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if hashmap[popped] != char:
                    return False
    return not stack

# def isValid( s: str) -> bool:
#     d = {')': '(', '}': '{', ']': '['}
#     stack = []
#     for c in s:
#         if c in d.keys() and (d[c] not in stack or stack[-1] != d[c]):
#             return False
#         elif c not in d.keys():
#             stack.append(c)
#         elif stack[-1] == d[c]:
#             stack.pop()
#     return True if stack == [] else False



        

print(isValid(s = '[{)]'))

