class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}  
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in bag:
                past_index = bag[complement]
                current_index = i
                return [past_index, current_index]
            
            else:
                bag[num] = i
                
        return []