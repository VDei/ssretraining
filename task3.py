# 1. Написати функцію to_minutes, яка для заданого числа годин повертає кількість хвилин. Наприклад, to_minutes(1.5) поверне 90.

def to_minutes(hours):
    return hours * 60ß

# 2. Написати функцію to_hours, яка для заданої кількості хвилин повертає кількість годин у вигляді десяткового дробу.
# У випадку нескінченного дробу заокруглювати до 4 знаків після коми.
# Наприклад, to_hours(12) повертає 0.2, to_hours(5) повертає 0.0833.

def to_hours(minutes):
    return round((minutes / 60), 4)

# 3. Написати функцію is_whole_div, яка перевіряє, чи число ділиться на інше число без остачі.
# Наприклад, is_whole_div(2, 3) поверне false, is_whole_div(12, 3) поверне true,

def is_whole_div(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
