
def cube_at_multiples_of_three(numbers):
    for index in range(len(numbers)):
        
        if index % 3 == 0:
            numbers[index] = numbers[index] ** 3
    return numbers


user_list = [3, 5, 5, 2, 8, 9, 7, 21, 6, 5, 4]


print("Original List: ", user_list)


transformed_list = cube_at_multiples_of_three(user_list)
print("Transformed List:", transformed_list)
