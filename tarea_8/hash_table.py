class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tabla = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in tabla:
                return [tabla[complemento], i]

            tabla[num] = i