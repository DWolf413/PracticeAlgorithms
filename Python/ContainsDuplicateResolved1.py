class Solution:
  def containsDuplicate(self, nums) -> bool:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          return True
    return False # if no duplicates are found, return false

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.containsDuplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.containsDuplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.containsDuplicate(nums3)) # Expected output: False

  nums4 = [3, 2, 6, -1, 2, 1]
  print(sol.containsDuplicate(nums4)) # Expected output: True
