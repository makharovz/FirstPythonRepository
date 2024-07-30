# Функция print() в Python используется для вывода данных на экран.

print("Hello, World!")
# => Hello, World!

print('Hello, World!')
# => Hello, World!

print('Hello', 'World!')
# => Hello World!

print("Hello", "World!", sep="-")
# => Hello-World! // sep (separator): Разделитель между аргументами.

print("Hello", "World", end="!\n")
# => Hello World! // end: Заключительный символ (по умолчанию новая строка) // \n - симмвол новой строки

print("Hello", "World", sep=', ', end='!\n')
# => Hello, World! // разделение с ", " // окончание "!" // перенос на новую строку

word = 'Python'
print(f'Hello, {word}!')
# => Hello, Python! // Использование f-строк (f-strings).

x = [0, 1, 2, 3, 4]
print(x)
# => 0, 1, 2, 3, 4 // Вывод объектов и строковых представлений.

y = [5, 6, 7, 8, 9]
print(y)
# => 5, 6, 7, 8, 9 // Вывод объектов и строковых представлений.