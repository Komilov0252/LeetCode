from typing import List
def maxArea( height: List[int]) -> int:
    left = 0
    right = len(height) -1
    square = 0
    result = 0
    while True:
        if left == right:
            return result
        square = min(height[left], height[right])*(right-left)
        if result < square:
            result = square
        if height[left] <= height[right]:
            left +=1
        else:
            right -=1
    return result


print(maxArea(height = [1,8,6,2,5,4,8,3,7]))





