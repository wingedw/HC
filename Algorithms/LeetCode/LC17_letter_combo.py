'''Given a string containing digits from 2-9 inclusive, return all possible
 letter combinations that the number could represent. Return the answer in 
 any order.  A mapping of digit to letters (just like on the telephone 
 buttons) is given below. Note that 1 does not map to any letters.'''

def letterCombinations(digits):
        digit_char = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']

        if digits == '': return []

        for digit in digits:
            letter = digit_char[int(digit)-2]
            res = append_letter(res, letter)
        return res
    
def append_letter(res, letters:str):
    _res = []
    for l in letters:
        for r in res:
            _res.append(r + l)
    return _res


print (letterCombinations('23'))