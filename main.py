original_text = input("Введите сообщение: ")
print(f"раскраска:\u001b[35m {original_text} \u001b[0m ")

lenght_text = len(original_text)
print(f"Количество символов в строке: {lenght_text}")
second_letter = original_text[1]
print(f"Второй символ строки: {second_letter}")
last_letter = original_text[-1]
print(f"Последний символ строки: {last_letter}")
first_three_letters = original_text[0:3]
print(f"Первые три символа: {first_three_letters}")
last_three_letter = original_text[-3:]
print(f"Последние три символа: {last_three_letter}")
color_start = int(input("Откуда закрашивать: "))
color_end = int(input("До куда закрашивать: "))
color_name = input("Выберете цвет: ")
if color_name == "синий":
    print(f"{original_text[:color_start]}\u001b[34m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
elif color_name == "красный":
    print(f"{original_text[:color_start]}\u001b[31m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
elif color_name == "зеленый":
    print(f"{original_text[:color_start]}\u001b[32m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
else:
    print(f"{original_text[:color_start]}\u001b[36;1m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
old_char = input("Введите символ, который хотите заменить: ")
new_char = input("Введите символ, на который хотите заменить: ")
modified_text = original_text.replace(old_char, new_char)
print(modified_text)
even_chars = modified_text[1::2]
print(f"Срез по чётным символам: {even_chars}")
odd_chars = modified_text[::2]
print(f"Срез по нечётным символам: {odd_chars}")
reversed_text = original_text[::-1]
print(reversed_text)
middle_index = len(original_text)//2
swapped_text = original_text[middle_index:]+original_text[:middle_index]
print(swapped_text)