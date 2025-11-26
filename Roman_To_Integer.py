class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        list_romans = list(s)
        dict_vals = {"I": 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000}
        num_int = 0
        val_ant = 0
        for i in reversed(list_romans):
            if dict_vals[i] < val_ant:
                num_int -= dict_vals[i]
            elif dict_vals[i] >= val_ant:
                num_int += dict_vals[i]
            val_ant = dict_vals[i]
        return num_int


solution = Solution
print(solution.romanToInt("MCMXCIV"))