"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens


def get_odd_indices(items):
    result = []

    for i, item in enumerate(items):
        if i % 2 != 0:
            result.append(item)
    
    return result


def print_as_numbered_list(items):
    count = 1
    for item in items:
        print(count,item)
        count +=1



def get_range(start, stop):
    nums = []

    num = int(start)

    while num < int(stop): 
        nums.append(num)
        num += 1

    return nums 


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper() + word[1:])

    return ''.join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
            
    return longest



def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):

    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ")":
            parens = parens - 1

        if parens < 0:
            return False

    return parens == 0 

def compress(string):
    compressed = []

    currChar  = ''
    charCount = 0

    for i, char in enumerate(string):
        if char != currChar:
            compressed.append(currChar)

            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0

        charCount += 1

    compressed.append(currChar)

    if charCount > 1: 
        compressed.append(str(charCount))

    return ''.join(compressed)
