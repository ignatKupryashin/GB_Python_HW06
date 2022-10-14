from functools import reduce
# ("Задание 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")


# Было

def task_3():
    test_list = [1.1, 1.2, 3.1, 5, 10.01]

    def dif_fraction_part(array):
        min_value = 1
        max_value = 0
        for i in range(len(array)):
            current_number = array[i] % 1
            if current_number != 0:
                if current_number > max_value:
                    max_value = current_number
                elif current_number < min_value:
                    min_value = current_number
        return round(max_value - min_value, 2)
    print(dif_fraction_part(test_list))

# Стало
def new_task3():
    test_list = [1.1, 1.3, 3.1, 5.15, 10.01]
    test_list = list(map(float, test_list))
    max_value = reduce(lambda x, y: x if (x > y) else y, map(lambda i: i % 1, test_list))
    min_value = reduce(lambda x, y: x if (x < y) else y, map(lambda i: i % 1, test_list))
    print(round((max_value - min_value) , 5))
new_task3()