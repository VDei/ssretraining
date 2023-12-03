"""
Написати функцію, яка отримає два аргументи - рядок str, що складається з цифр, та число n. Ця функція буде повертати перетворений рядок. Агоритм перетворення такий:
 1. Розбити рядок на частини розміру n (якщо остання частина менше за n, то її просто відкинути).
 2. Кожну частину перетворити таким чином: якщо сума кубів кожної цифри - парне число, то перевернути цю частину (записати "задом наперед"), інакше - перемістити першу цифру на останню позицію.
 3. Зібрати отримані частини разом.
У випадку, якщо n - недодатнє число або
"""


def convert(string_of_digits, n):
    if n <= 0 or n > len(string_of_digits) or len(string_of_digits) == 0:
        return ""

    digits = [
        string_of_digits[i : i + n]
        for i in range(0, len(string_of_digits) - len(string_of_digits) % n, n)
    ]

    def cubes(cut_string):
        sum_of_cubes = sum(int(digit) ** 3 for digit in cut_string)
        if sum_of_cubes % 2 == 0:
            return cut_string[::-1]
        else:
            return cut_string[1:] + cut_string[0]

    return "".join(cubes(cut_string) for cut_string in digits)


# print(convert("123456987654", 6))
