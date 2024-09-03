#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                dp[i][j] = dp[i][j] or \
                    (i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]) or \
                    (j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1])

        return dp[0][0]

# @lc code=end

