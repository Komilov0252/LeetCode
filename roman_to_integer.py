def romanToInt( s: str) -> int:
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    previous = 0
    for i in reversed(s):
        if roman_to_int[i] < previous:
                result -= roman_to_int[i]
        else: 
                result += roman_to_int[i]
        previous = roman_to_int[i]
    return result

print(romanToInt('III'))
    
