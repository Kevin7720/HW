# -*- coding: utf-8 -*-
"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, 
where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings

A valid parentheses string S is primitive if it is nonempty, 
and there does not exist a way to split it into S = A+B, 
with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, 
consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, 
where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive 
string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"

Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""
class Solution(object):
    def removeOuterParentheses(self, S):
        if len(S) == 0:
            return ""
        count = 1
        temp = [0]
        for i in range(1,len(S)):
            if count == 0:
                temp.append(i)
            if '(' == S[i]:
                count = count + 1
            else:
                count = count - 1
            if count == 0:
                temp.append(i)    
        res = ""
        for i in range(len(temp)/2):
            res = res + S[temp[2*i]+1:temp[2*i+1]]           
        return res

