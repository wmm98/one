class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            left, right = S[i-len(S)::-1].find(C), S[i:].find(C)
            if left == -1:
                left = 10000  # 认为10000已经足够大（字符串总长）
            if right == -1:
                right = 10000
            res.append(min(left, right))
        return res

S = "loveleetcode"
C = 'e'
result = Solution()
print(result.shortestToChar(S, C))