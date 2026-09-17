
user_input = input("Enter numbers separated by spaces: ")


original_list = [int(num) for num in user_input.split()]


divisible_list = [3,5]


for num in original_list:
   
    if num % 3 == 0 and num % 5 == 0:
        divisible_list.append(num)


print("Numbers divisible by 3 and 5:", divisible_list)
