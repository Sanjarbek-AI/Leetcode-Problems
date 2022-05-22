class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp_str = ""
        for num in digits:
            temp_str += str(num)

        temp_int = int(temp_str) + 1
        temp_str = str(temp_int)
        result = list()

        for char in temp_str:
            result.append(int(char))
        return result


a = Solution()
a.plusOne([1, 2, 3])
