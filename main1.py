numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_numbers = [0 if el is None else el for el in numbers]
sr = sum(new_numbers) / len(new_numbers)
fin_numbers = [sr if el is None else el for el in numbers]

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", fin_numbers)