'''
Difficulty: Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''Easy and Slower Way:

        digits = map(str, digits)
        digits = ''.join(digits)
        digits = int(digits) + 1
        digits = str(digits)
        digits = list(digits)
        digits = list(map(int, digits))
        return digits'''

        # If no map or join ability
        lenD = len(digits)
        for i, d in enumerate(reversed(digits)):
            if d >= 9:
                if i == lenD - 1:
                    digits[0] = 0
                    digits.insert(0, 1)
                else:
                    digits[lenD - i - 1] += 1
                    digits[lenD - 1 - i] = 0
            else:
                digits[lenD - 1 - i] += 1
                break
        return digits


examples = [{
    'input' : [1, 2, 3],
    'answer': [1, 2, 4]
}, {
    'input' : [4, 3, 2, 1],
    'answer': [4, 3, 2, 2]
}, {
    'input' : [1],
    'answer': [2]
}, {
    'input' : [9],
    'answer': [1, 0]
}, {
    'input' : [9, 9],
    'answer': [1, 0, 0]
}]

for i, e in enumerate(examples):
    if i == i:
        print('--------------------------------------------')
        print('Example: ' + str(i + 1))
        print(e['input'])
        return_val = Solution.plusOne("", e['input'])
        print(return_val == e['answer'])
        print(return_val)
        print(e['answer'])
