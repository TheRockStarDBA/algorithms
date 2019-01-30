""" 60. Permutation Sequence - Medium
Topic: Math, Backtracking
Related: Next Permutation - Medium
        Permutations - Medium
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
 """

import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        factorial = math.factorial(n - 1)
        result = ""
        permutation = [i for i in range(1, n + 1)]

        for i in reversed(range(n)):
            current = permutation[int(k / factorial)]
            result += str(current)
            permutation.remove(current)
            if i > 0:
                k %= factorial
                factorial /= i

        return result


if __name__ == "__main__":
    result = Solution().getPermutation(4, 9)
    print(result)