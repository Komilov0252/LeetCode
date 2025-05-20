from typing import List
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    result = float('inf')
    for index, value in enumerate(nums):
        if index > 0 and nums[index-1] == value:
            continue
        left = index + 1
        right = len(nums) -1
        while right > left:
            res = value + nums[left] + nums[right]
            if abs(res-target) < abs(result-target):
                result = res
            if res > target:
                right -= 1
            elif res < target:
                left += 1
            else:
                result = res
                break
            
    return result


print(threeSumClosest(nums = [1,1,1,0], target = 100))
