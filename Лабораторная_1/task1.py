numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num_1 = numbers[:4]
num_2 = numbers[5:]

sum_num = num_1 + num_2

None_1 = float (sum(sum_num) / len(numbers))

numbers[4] = None_1

print("Измененный список:", numbers)
