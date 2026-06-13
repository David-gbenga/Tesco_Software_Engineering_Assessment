"""
Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

Example

Input

code = A1b2B!a
Output

1
"""
def isAlphabeticPalindrome(code):
    alphabets = "".join(letter.lower() for letter in code if letter.isalpha())
    return 1 if alphabets == alphabets[::-1] else 0


if __name__=="__main__":
    
    code = "A1b2B!a"
    
    result = isAlphabeticPalindrome(code)
    
    print(result)
    