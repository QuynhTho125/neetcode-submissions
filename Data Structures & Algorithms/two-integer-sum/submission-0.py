"""fruits = ['táo', 'lê', 'đào']
# i sẽ tự tăng từ 0, 1, 2... còn fruit sẽ lấy giá trị 'táo', 'lê', 'đào'
for i, fruit in enumerate(fruits):
    print(f"Vị trí {i} là {fruit}")"""

#return smaller index not smaller value

class Solution:
    def twoSum(self, nums:List(int), target:int) -> List(int):
        seen={}
        for i, num in enumerate(nums): #hai vế "for i, num" và "in enumerate(nums)"
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
