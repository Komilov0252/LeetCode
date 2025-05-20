from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for index, v in enumerate(nums):
        if index > 0 and nums[index-1] == v:
            continue
        left, right = index + 1, len(nums) - 1
        while left < right:
            res = v + nums[left] + nums[right]
            if res > 0:
                right -= 1
            elif res < 0:
                left += 1
            else:
                result.append([v, nums[left], nums[right]])
                left+=1
                while nums[left] == nums[left-1] and right >left:
                    left +=1
    return result


print(threeSum(nums = [-1,0,1,2,-1,-4]))

