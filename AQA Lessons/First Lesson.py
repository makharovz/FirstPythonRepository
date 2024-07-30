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

num1 = 1
num2 = 3
result = num1+num2
print(result)