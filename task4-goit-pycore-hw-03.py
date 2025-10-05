# КОСТЯНТИН ЛЕМЕШОК, ДЗ № 3 ДО КУРСУ PYTHON CORE

# Завдання 4

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.


# Вимоги до завдання:

#     Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
#     Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
#     Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


# Рекомендації для виконання:

#     Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
#     Визначте поточну дату системи за допомогою datetime.today().date().
#     Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
#     Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
#     Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
#     Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
#     Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
#     Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.


# Критерії оцінювання:

#     Актуальність та коректність визначення днів народження на 7 днів вперед.
#     Правильність обробки випадків, коли дні народження припадають на вихідні.
#     Читабельність та структурованість коду.

from datetime import datetime, timedelta
import logging

# Configure logging to show only the message
logging.basicConfig(format="%(message)s", level=logging.ERROR, force=True)

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Returns a list of users whose birthdays are within the next 7 days, including today.
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday.
        :param users: List of dictionaries with keys 'name' and 'birthday' (format 'YYYY.MM.DD')
        :return: List of dictionaries with keys 'name' and 'congratulation_date' (format 'YYYY.MM.DD')
    """
    today = datetime.today().date()
    result = []

    for user in users:
        try:
            # Convert birthday string to datetime.date
            birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except KeyError:
            logging.error(f"User entry missing 'birthday' or 'name': {user}")
            continue
        except ValueError:
            logging.error(f"Invalid birthday format for user {user.get('name', 'unknown')}: {user.get('birthday')}")
            continue

        # Adjust birthday to this year
        birthday_this_year = birthday_date.replace(year=today.year)

        # If birthday already passed this year, use next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate days until birthday
        delta_days = (birthday_this_year - today).days

        # Only consider birthdays within the next 7 days including today
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # If birthday falls on weekend, move to next Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user.get("name", "unknown"),
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result