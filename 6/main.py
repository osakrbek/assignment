# Exercise 1: two-sum
num1 = 5
num2 = 7
sum_result = num1 + num2
print("Exercise 1 - Sum:", sum_result)

# Exercise 2: reverse-string
original_string = "hello"
reversed_string = original_string[::-1]
print("Exercise 2 - Reversed String:", reversed_string)

# Exercise 3: string-length
test_string = "hello"
string_length = len(test_string)
print("Exercise 3 - String Length:", string_length)

# Exercise 4: concatenate-string
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print("Exercise 4 - Concatenated String:", concatenated_string)

# Exercise 5: is-vowel
char = "e"
is_vowel = char.lower() in "aeiou"
print("Exercise 5 - Is Vowel:", is_vowel)

# Exercise 6: swap-first-last
swap_string = "python"
if len(swap_string) > 1:
    swapped_string = swap_string[-1] + swap_string[1:-1] + swap_string[0]
else:
    swapped_string = swap_string
print("Exercise 6 - Swapped String:", swapped_string)

# Exercise 7: to-uppercase
lowercase_string = "python"
uppercase_string = lowercase_string.upper()
print("Exercise 7 - Uppercase String:", uppercase_string)

# Exercise 8: rectangle-area
length = 10
width = 5
rectangle_area = length * width
print("Exercise 8 - Rectangle Area:", rectangle_area)

# Exercise 9: is-even
number = 42
is_even = number % 2 == 0
print("Exercise 9 - Is Even:", is_even)

# Exercise 10: extract-first-three
extract_string = "hello"
first_three_chars = extract_string[:3]
print("Exercise 10 - First Three Characters:", first_three_chars)

# Exercise 11: string-interpolation
name = "John"
age = 30
message = f"My name is {name} and I am {age} years old."
print("Exercise 11 - Interpolated Message:", message)

# Exercise 12: string-slicing
slicing_string = "hello world"
sliced_string = slicing_string[2:6]
print("Exercise 12 - Sliced String:", sliced_string)

# Exercise 13: type-conversion
number_as_string = "123"
converted_number = int(number_as_string)
print("Exercise 13 - Converted Number:", converted_number)

# Exercise 14: string-repetition
repeat_string = "ha"
repeated_string = repeat_string * 3
print("Exercise 14 - Repeated String:", repeated_string)

# Exercise 15: calculate-quotient-remainder
num1 = 20
num2 = 3
quotient = num1 // num2
remainder = num1 % num2
print("Exercise 15 - Quotient:", quotient, "Remainder:", remainder)

# Exercise 16: float-division
num1 = 10
num2 = 3
float_division = num1 / num2
print("Exercise 16 - Float Division:", float_division)

# Exercise 17: string-methods
count_string = "hello world"
count_char = count_string.count("o")
print("Exercise 17 - Count of 'o':", count_char)

# Exercise 18: escape-sequences
escape_string = 'He said, "Hello!"'
print("Exercise 18 - Escaped String:", escape_string)

# Exercise 19: multi-line-string
multi_line = """This is a
multi-line string
example."""
print("Exercise 19 - Multi-line String:\n", multi_line)

# Exercise 20: exponentiation
base = 2
exponent = 3
exponent_result = base**exponent
print("Exercise 20 - Exponentiation Result:", exponent_result)

# Exercise 21: check-palindrome
palindrome_string = "racecar"
is_palindromic = palindrome_string == palindrome_string[::-1]
print("Exercise 21 - Is Palindromic:", is_palindromic)

# Exercise 22: check-anagrams
string_a = "spar"
string_b = "rasp"
are_anagrams = sorted(string_a.lower()) == sorted(string_b.lower())
print("Exercise 22 - Are Anagrams:", are_anagrams)
