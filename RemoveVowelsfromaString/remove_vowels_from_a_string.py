def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    # Example Usage:
    test_string1 = "Hello World"
    print(f"Original: '{test_string1}'")
    print(f"Without vowels: '{remove_vowels(test_string1)}'")

    test_string2 = "Programming is Fun"
    print(f"Original: '{test_string2}'")
    print(f"Without vowels: '{remove_vowels(test_string2)}'")

    test_string3 = "AEIOUaeiou"
    print(f"Original: '{test_string3}'")
    print(f"Without vowels: '{remove_vowels(test_string3)}'")

    test_string4 = "Python"
    print(f"Original: '{test_string4}'")
    print(f"Without vowels: '{remove_vowels(test_string4)}'")

    test_string5 = ""
    print(f"Original: '{test_string5}'")
    print(f"Without vowels: '{remove_vowels(test_string5)}'")

    test_string6 = "Rhythm" # No vowels
    print(f"Original: '{test_string6}'")
    print(f"Without vowels: '{remove_vowels(test_string6)}'")