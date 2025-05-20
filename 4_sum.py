from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result, temp = [], []
    for i, v in enumerate(nums):
        if i > 0 and nums[i-1] == v:
            continue
        j = len(nums)-1
        while j>i:
            left = i+1
            right = j-1
            while right>left:
                sum = v + nums[j]+nums[left]+nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left +=1
                else:
                    temp.append([v,nums[left],nums[right],nums[j]])
                    left += 1
                    while nums[left] == nums[left-1] and right > left:
                        left+=1
            j -=1
            while nums[j] == nums[j+1] and i < j:
                j -=1
    return temp


print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))

