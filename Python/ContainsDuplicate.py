class Solution:
    def containsDuplicate(self, nums):
        
        results = nums
               
        for i in range(len(nums)):           
                      
            for j in range(i + 1, len(results)):
                if nums[i] == nums[j]:
                    return True


        return False


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.containsDuplicate([1,2,1,4]))
    