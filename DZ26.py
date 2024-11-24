#1 Задание
def calculate_numbers(num1, num2, num3):
    total_sum = num1 + num2 + num3

    product = num1 * num2 * num3

    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)

    print("Сумма:", total_sum)
    print("Произведение:", product)
    print("Наибольшее число:", maximum)
    print("Наименьшее число:", minimum)

calculate_numbers(3, 5, 2)

#2 Задание
def analyze_string(input_string):

    words = input_string.split()

    total_words = len(words)

    long_words_count = sum(1 for word in words if len(word) > 2)

    print("Введенная строка:", input_string)
    print("Количество слов в строке:", total_words)
    print("Количество слов с более чем 2 символами:", long_words_count)
    print("Строка в нижнем регистре:", input_string.lower())
    print("Строка в верхнем регистре:", input_string.upper())

user_input = input("Введите строку: ")
analyze_string(user_input)

#3 Задание

original_list = [1, 30, 30, 25, 24, 30, 1, 27, 25, 40]

unique_numbers = list(set(original_list))
print("Уникальные числа:", unique_numbers)

new_list = [num for num in unique_numbers if num > 24]
print("Числа больше 24:", new_list)

even_dict = {str(index + 1): num for index, num in enumerate(new_list) if num % 2 == 0}
print("Словарь с четными числами:", even_dict)

#4 Задание

def centimeters_to_meters(centimeters):

    meters = centimeters / 100
    return meters

user_input = float(input("Введите количество сантиметров: "))
result = centimeters_to_meters(user_input)
print(f"{user_input} сантиметров равно {result} метров.")

#5 Задание

def convert_minutes_to_hours_and_minutes(minutes):

    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours} час(ов) {remaining_minutes} минут(ы)"

user_input = int(input("Введите количество минут: "))
result = convert_minutes_to_hours_and_minutes(user_input)
print(result)

#6 Задание

def calculate_sum_and_product_of_digits(number):
    if 100 <= number <= 999:

        digits = [int(digit) for digit in str(number)]
        digit_sum = sum(digits)
        digit_product = 1
        for digit in digits:
            digit_product *= digit
        return f"Сумма цифр = {digit_sum}, Произведение цифр = {digit_product}"
    else:
        return "Введите положительное трехзначное число."

user_input = int(input("Введите положительное трехзначное число: "))
result = calculate_sum_and_product_of_digits(user_input)
print(result)

#7 Задание

def is_number_in_range(x, a, b):

    if a > b:
        a, b = b, a
    return a <= x <= b

x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if is_number_in_range(x, a, b):
    print(f"Число {x} принадлежит промежутку от {a} до {b}.")
else:
    print(f"Число {x} не принадлежит промежутку от {a} до {b}.")

#8 Задание

def create_dict_from_strings(txt_1, txt_2):
    if len(txt_1) == len(txt_2):
        return {txt_1[i]: int(txt_2[i]) for i in range(len(txt_1))}
    else:
        return "Строки должны иметь одинаковую длину."

txt1 = 'abcde'
txt2 = '12345'
result = create_dict_from_strings(txt1, txt2)
print(result)

#9 Задание

def collect_user_info(full_name, age, phone_number):

    if age < 1 or age > 150:
        print("Возраст должен быть от 1 до 150 лет. Установлено значение 0.")
        age = 0

    if len(phone_number) < 4 or len(phone_number) > 11:
        print("Номер телефона должен содержать от 4 до 11 символов. Установлено значение 8-000-000-00-00.")
        phone_number = "8-000-000-00-00"

    user_info = {
        "ФИО": full_name,
        "Возраст": age,
        "Номер телефона": phone_number
    }

    return user_info

full_name = input("Введите ваше ФИО: ")
age = int(input("Введите ваш возраст: "))
phone_number = input("Введите ваш номер телефона: ")

result = collect_user_info(full_name, age, phone_number)

print(result)


#10 Задание

text = "Python is the best programming language"

length = len(text)
print("Количество символов в строке:", length)

first_character = text[0]
print("Первый элемент строки:", first_character)

last_character = text[-1]
print("Последний элемент строки:", last_character)

first_word = text.split()[0]
print("Первое слово этой строки:", first_word)

last_word = text.split()[-1]
print("Последнее слово этой строки:", last_word)

programming = text[20:31]
print("Слово 'programming':", programming)


#11 Задание

def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Ошибка: неизвестная операция!"

operation = input("Введите операцию (add, subtract, multiply, divide): ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = calculator(operation, a, b)
print("Результат:", result)
