# КОСТЯНТИН ЛЕМЕШОК, ДЗ № 3 ДО КУРСУ PYTHON CORE

# Завдання 1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:

#     Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#     Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
#     У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
#     Для роботи з датами слід використовувати модуль datetime Python.


# Рекомендації для виконання:

#     Імпортуйте модуль datetime.
#     Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
#     Отримайте поточну дату, використовуючи datetime.today().
#     Розрахуйте різницю між поточною датою та заданою датою.
#     Поверніть різницю у днях як ціле число.


# Критерії оцінювання:

#     Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
#     Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
#     Читабельність коду: код повинен бути чистим і добре документованим.


# Приклад:

#     Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути −157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.

from datetime import datetime
import logging

# Configure logging so that only the message is printed (no ERROR:root prefix)
logging.basicConfig(format="%(message)s", level=logging.ERROR, force=True)

def get_days_from_today(target_date: str) -> int:
    """
    Counts number of days between today's date and target date
        :param target-date: String formatted as YYYY-MM-DD
        :return: Integer (negative if target_date > today)
    """
    
    try:
        # Convert string date into datetime date
        target_date_dt = datetime.strptime(target_date, "%Y-%m-%d").date()
        
        # Today's date (without time part)
        today = datetime.today().date()

        # Difference in days (positive if past, negative if future)
        delta = today - target_date_dt
        return delta.days

    except ValueError:
        # Show error message if date format is wrong
        logging.error("Wrong date input. Use YYYY-MM-DD format.")


# Run interactive loop only when script is executed directly
if __name__ == "__main__":
    while True:
        # Strip off spaces and quote characters from user input, convert it to lowercase
        user_input = input(f"Enter date in YYYY-MM-DD format to calculate number of days from today. Or enter 'q' to exit: ").strip(" '\"\t\n\r").lower()
        
        # exit if input is q/Q
        if user_input == 'q':
            print('Program exited.')
            break
        
        # Calculate days difference if input is a valid date
        else:
            delta_days = get_days_from_today(user_input)
            if delta_days is not None:
                print(f"Difference between today's date and {user_input} is {delta_days} days.")