nums = []

while True:
    user_input = int(input("Введите числа для заполнения списка, если закончили впишите 777777: "))
    if user_input == 777777:
        break
    else:
        nums.append(user_input)
target = int(input("Введите цель: "))
a = 0
for i in range(len(nums)-1):
    first_number = nums[i]
    if a == 1:
        break
    for a in range(len(nums)):
        second_number = nums[a]
        if first_number != second_number:
            if first_number + second_number == target:
                print([nums[i],nums[a]])
                a = 1
                break#Done