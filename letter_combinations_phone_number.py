from typing import List
def letterCombinations1(digits: str) -> List[str]:
    letter_map = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz',
        }
    if digits == '':
        return []
    ans, sol = [], []
    n = len(digits)
    def backtrack(i=0):
        if i == n:
            ans.append(''.join(sol))
            return 
        for letter in letter_map[digits[i]]:
            sol.append(letter)
            backtrack(i+1)
            sol.pop()
    backtrack(0)
    return ans

print(letterCombinations1(digits= '233'))


# def letterCombinations2(digits: str) -> List[str]:
#     dic = {"2": ["a","b","c"]
#                 , "3": ["d","e","f"]
#                 , "4": ["g","h","i"]
#                 , "5": ["j","k","l"]
#                 , "6": ["m","n","o"]
#                 , "7": ["p","q","r", "s"]
#                 , "8": ["t","u","v"]
#                 , "9": ["w","x","y", "z"]}
#     res = []
#     for digit in digits:
#         temp = dic[digit]
#         if res == []:
#             res = temp
#         else:
#             temp1 = []
#             for i in res:
#                 for j in temp:
#                      temp1.append(i+j)
#                 res = temp1
#     return res

# print(letterCombinations2(digits= '233'))