'''
Difficulty: Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = 0
        lenS = len(S)
        ti = 0
        lenT = len(T)
        modS = []
        modT = []
        while True:
            # print(modS, modT)
            if si < lenS:
                if S[si] != '#':
                    modS.append(S[si])
                else:
                    if len(modS) >= 1:
                        del modS[-1]
                si += 1
            if ti < lenT:
                if T[ti] != '#':
                    modT.append(T[ti])
                else:
                    if len(modT) >= 1:
                        del modT[-1]
                ti += 1
            if si == lenS and ti == lenT:
                break
        # print(modS, modT, si, ti)
        if modS == modT:
            return True
        else:
            return False

        '''"ab#c"
"ad#c"
"ab##"
"c#d#"
"a##c"
"#a#c"'''
