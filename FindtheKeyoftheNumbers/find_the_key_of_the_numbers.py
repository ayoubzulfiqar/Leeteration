def find_key(num1, num2, num3):
    s_num1 = str(num1).zfill(4)
    s_num2 = str(num2).zfill(4)
    s_num3 = str(num3).zfill(4)

    key_digits = []
    for i in range(4):
        digit1 = int(s_num1[i])
        digit2 = int(s_num2[i])
        digit3 = int(s_num3[i])
        
        min_digit = min(digit1, digit2, digit3)
        key_digits.append(str(min_digit))
    
    key_str = "".join(key_digits)
    return int(key_str)