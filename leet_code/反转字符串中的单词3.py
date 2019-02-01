'''给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。'''


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_split = s.split()
        result1 = ""
        for i in s_split:
            i = i[::-1]
            print(i)
            result1 = result1 + i + " "
        return result1[:-1]

        # 百度答案
        # ans = s.split()
        # res = []
        # for item in ans:
        #     res.append(item[::-1])
        #     print(res)
        # return ' '.join(res)

s = "Let's take LeetCode contest"
result = Solution()
print(result.reverseWords(s))
