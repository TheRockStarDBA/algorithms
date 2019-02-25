""" 93. Restore IP Addresses - Medium
Topic: string, backtracking

Given a string containing only digits, restore it by returning all possible valid
IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"] """


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(s, 0, [], result)
        return result

    def dfs(self, s, length, ips, result):
        if not s:
            if length == 4:
                result.append('.'.join(ips))
            return
        elif length == 4:
            return

        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1:
                    self.dfs(s[i:], length + 1, ips + [s[:i]], result)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], length + 1, ips + [s[:i]], result)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], length + 1, ips + [s[:i]], result)


if __name__ == "__main__":
    s = "25525511135"
    result = Solution().restoreIpAddresses(s)
    print(result)