from typing import List
def longestCommonPrefix( strs: List[str]) -> str:
    signal = 'green'
    min_value = min(strs, key=len)
    res = ""
    for i in range(len(min_value)):
        for j in range(len(strs)):
            if min_value[i] != strs[j][i]:
                signal = 'red'
                break
            if j == len(strs)-1:
                res += min_value[i]
        if signal == 'red':
            break
    return res
        


print(longestCommonPrefix(strs = ["dog","racecar","car"]))