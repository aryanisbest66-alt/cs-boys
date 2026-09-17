def is_palindrome_string(num):
    return str(num) == str(num)[::-1]

number = 67
if is_palindrome_string(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
