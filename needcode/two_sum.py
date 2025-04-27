class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    temp = {}
    for i in range(len(nums)):
      if target - nums[i] in temp: 
        return [temp[target-nums[i]], i]
      else: 
        temp[nums[i]] = temp.get(nums[i], i)
    
solution = Solution()


nums = [3, 4, 5, 6]
target = 7

print(solution.twoSum(nums, target))
print("right output:", [0, 1])
        