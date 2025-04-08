class Solution:
    def runningSum(self, nums):
        
        result = [0] * len(nums)
        result[0] = nums[0]
       
        for i in range(len(nums)-1):
            result[i+1] = result[i] + nums[i+1]

        return result


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.runningSum([1,1,1,1]))
    