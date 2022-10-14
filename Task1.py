def title(title_string):
    print("\n" + title_string + "\n")



# Первоначальный вариант
def task_1():
    title("Задание 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")
    test_list = [1, 8, 12, 4, 115, 23]
    print(f"Первоначальный список: {test_list}")

    def odd_position_sum(array):
        answer = 0
        for i in range(0, len(array)):
            if i % 2 == 0:
                answer += array[i]
        return answer

    print(f"Ответ: {odd_position_sum(test_list)}")


# Новый вариант
def new_Task1():
    title("Задание 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")
    test_list = [1, 8, 12, 4, 115, 23]
    new_list = [test_list[x] for x in range(len(test_list)) if x % 2 == 0]
    print(new_list)


new_Task1()