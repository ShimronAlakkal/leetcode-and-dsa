# the problem here is that i used my own code, it should've been the completion of the code already given by leetcode

class Solution:
    def __init__(self, prompt):
        self.prompt_string = prompt
        self.constants = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

    def convert_to_number(self):
        number = 0
        for letter in self.prompt_string: 
            for key in self.constants.keys():
                if letter == key:
                    number += self.constants[key]
        return number


if __name__ == '__main__':
    print(Solution("LVIII").convert_to_number())


# the following is a better answer

class Solution:

    def romanToInt(self, S: str) -> int:
        constants = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        number = 0
        for letter in S: 
            for key in constants.keys():
                if letter == key:
                    number += constants[key]
        return number
