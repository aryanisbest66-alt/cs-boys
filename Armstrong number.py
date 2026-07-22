def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
   
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    
    return digit_sum == number


user_input = int(input("Enter an integer: "))

if is_armstrong(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
