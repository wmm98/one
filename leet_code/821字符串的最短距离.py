'''给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:

字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。'''


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distance_list = []
        same_C = []
        S1 = S
        while True:
            num = S1.find(C)
            if num != -1:
                same_C.append(num)
                S1 = S1.replace(C, " ", 1)
            else:
                break
        for i in range(len(S)):
            distance_list1 = []
            for j in same_C:
                distance = abs(i - j)
                distance_list1.append(distance)
            distance_list.append(min(distance_list1))
        return distance_list

S = "loveleetcode"
C = 'e'
result = Solution()
print(result.shortestToChar(S, C))

