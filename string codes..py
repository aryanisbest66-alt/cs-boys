# Take a string input from the user
user_string = input("Enter a string: ")

# Initialize counters for each category
uppercase_count = 0
lowercase_count = 0
vowel_count = 0
digit_count = 0
space_count = 0

# Define a set of vowels for efficient lookup (both upper and lower case)
vowels = set("aeiouAEIOU")

# Iterate through each character in the string
for char in user_string:
    # Check for uppercase letters
    if char.isupper():
        uppercase_count += 1
    # Check for lowercase letters
    elif char.islower():
        lowercase_count += 1
        
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1
        
    # Check for digits
    if char.isdigit():
        digit_count += 1
        
    # Check for spaces
    if char.isspace():
        space_count += 1

# Display the results
print("\n--- Character Analysis Results ---")
print(f"Uppercase letters : {uppercase_count}")
print(f"Lowercase letters : {lowercase_count}")
print(f"Vowels            : {vowel_count}")
print(f"Digits            : {digit_count}")
print(f"Spaces            : {space_count}")
