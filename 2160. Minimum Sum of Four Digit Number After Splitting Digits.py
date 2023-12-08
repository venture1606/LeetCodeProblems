class Solution:
    def minimumSum(self, num: int) -> int:
        string = str(num)
        number_list = sorted([int(x) for x in string])
        num1 = int(str(number_list[0]) + str(number_list[-1]))
        num2 = int(str(number_list[1]) + str(number_list[-2]))
        result = num1 + num2
        return result
