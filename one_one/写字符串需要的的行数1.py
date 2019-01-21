


class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        ch = [chr(i).lower() for i in range(65, 91)]
        result = 0
        flag = 1
        for i in S:
            i_index = ch.index(i)
            i_length = widths[i_index]
            result += i_length
            if result > 100:
                flag += 1
                result = widths[i_index]
        result_list = [flag, result]
        return result_list


widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "abcdefghijklmnopqrstuvwxyz"
one = Solution()
print(one.numberOfLines(widths, S))