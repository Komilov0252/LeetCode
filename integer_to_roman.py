from typing import List, AnyStr
def intToRoman(num: int) -> str:
    index = 0
    result = ''
    Roman = {1:'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    for key, value in reversed(Roman.items()):
        index = num//key
        result = result + (index*value)
        num = num%key
    return result
print(intToRoman(3749))
            
    
