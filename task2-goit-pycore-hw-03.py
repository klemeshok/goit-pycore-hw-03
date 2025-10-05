# КОСТЯНТИН ЛЕМЕШОК, ДЗ № 3 ДО КУРСУ PYTHON CORE

# Завдання 2

# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.


# Вимоги до завдання:

#     Параметри функції:

#     min - мінімальне можливе число у наборі (не менше 1).
#     max - максимальне можливе число у наборі (не більше 1000).
#     quantity - кількість чисел, які потрібно вибрати (значення між min і max).

#     Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
#     Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


# Рекомендації для виконання:

#     Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
#     Використовуйте модуль random для генерації випадкових чисел.
#     Використовуйте множину або інший механізм для забезпечення унікальності чисел.
#     Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


# Критерії оцінювання:

#     Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
#     Унікальність результату: усі числа у видачі повинні бути унікальними.
#     Відповідність вимогам: результат має бути у вигляді відсортованого списку.
#     Читабельність коду: код має бути чистим і добре документованим.

import random
import logging

# Configure logging so that only the message is printed (no ERROR:root prefix)
logging.basicConfig(format="%(message)s", level=logging.ERROR, force=True)


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """
    Generates a set of unique random numbers for a lottery ticket.
        :param min_num: Minimum possible number in the set (integer >=1)
        :param max_num: Maximum possible number in the set (integer <=1000)
        :param quantity: How many numbers to generate (integer between 1 and max_num-min_num+1)
        :return: Sorted list of unique numbers; empty list if input is invalid
    """

    # Check that input values are integers, reject other types
    if not (isinstance(min_num, int) and isinstance(max_num, int) and isinstance(quantity, int)):
        logging.error("All input parameters must be integers (floats and other types are not allowed).")
        return []

    # Check that input values are within valid ranges
    if not (1 <= min_num <= max_num <= 1000):
        logging.error("Invalid range: min_num must be >=1, max_num <=1000, and min_num <= max_num.")
        return []

    if not (1 <= quantity <= (max_num - min_num + 1)):
        logging_error_message = (
            "Invalid quantity: must be at least 1 and at most the number of possible numbers in the range.\n"
            f"With current min_num={min_num} and max_num={max_num}, quantity should be less or equal than {max_num - min_num + 1}."
        )
        logging.error(logging_error_message)
        return []

    # Generate unique random numbers
    numbers = random.sample(range(min_num, max_num + 1), quantity)

    # Return a sorted list
    return sorted(numbers)