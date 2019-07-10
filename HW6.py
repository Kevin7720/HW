# -*- coding: utf-8 -*-
"""
961. N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, 
and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
"""
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
