"""Завдання 1. У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії.
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму 
заробітної плати всіх розробників.
"""
salary_entries = [
    "Alex Korp,3000",
    "Nikita Borisenko,2000",
    "Sitarama Raju,1000",
    "Inna Keba,3500"]

with open("salary_data.txt", "w", encoding="utf-8") as file: # Створення файлу з даними про зарплати розробників
    for entry in salary_entries:
        file.write(entry + "\n")

def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            text_from_salary_data = file.read() # Читання вмісту файлу txt
        entries = text_from_salary_data.strip().split()  # Розбиваємо текст за пробілами, далі за комами
        salaries = []
        for entry in entries:
            try:
                name, salary = entry.split(",") # Розділення імені та даних по з/п по комі
                salaries.append(float(salary))
            except ValueError:  
                continue 
        total = int(sum(salaries))  # Розрахунок загальної з.п. приведений до цілого числа як в прикладі
        average = int(total / len(salaries)) if salaries else 0 # Розрахунок середньої з/п приведений до цілого числа
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
total, average = total_salary("salary_data.txt") 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


"""Критерії оцінювання:
1. Функція повинна точно обчислювати загальну та середню суми. - done. 
2. Повинна бути обробка випадків, коли файл відсутній або пошкоджений. - done. додано обробку помилок у функції except
3. Код має бути чистим, добре структурованим і зрозумілим."""