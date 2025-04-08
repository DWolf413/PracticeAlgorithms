class Solution:
  def contains_duplicate(self, nums) -> bool:
    nums.sort() # sort the array
    # use a loop to compare each element with its next element
    for i in range(len(nums) - 1):
      if nums[i] == nums[i + 1]: # if any two elements are the same, return true
        return True
    return False # if no duplicates are found, return false

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.contains_duplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.contains_duplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.contains_duplicate(nums3)) # Expected output: False

  nums4 = [3, 2, 6, -1, 2, 1]
  print(sol.contains_duplicate(nums4)) # Expected output: True
