
def title(title_string):
    print("\n" + title_string + "\n")

# Было
def task_2():
    title("Задание 2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
    test_list = [2, 3, 5, 6]
    def multiply_pair_index(array):
        new_array = []
        for i in range(len(array) // 2):
            new_array.append(array[i] * array[len(array) - 1 - i])
        return new_array
    print(multiply_pair_index(test_list))

# Стало
def new_task_2():
    title("Задание 2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
    test_list = [2, 3, 5, 6]
    new_array = [test_list[x] * test_list[0 - x - 1] for x in range(len(test_list) // 2)]
    print(new_array)

new_task_2()