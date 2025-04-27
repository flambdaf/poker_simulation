class Solution:
  def search(self, nums: list[int], target: int) -> int:
    min_num = 0
    max_num = len(nums) - 1 

    while (min_num <= max_num):
      average_num = (min_num + max_num) // 2
      if nums[average_num] == target:
        return average_num
      elif nums[average_num] < target:
        min_num = average_num + 1
      else: 
        max_num = average_num
    return -1
  


nums = list(range(0, 102, 3))
target = 0

binary_search = Solution()
print(binary_search.search(nums, target));


