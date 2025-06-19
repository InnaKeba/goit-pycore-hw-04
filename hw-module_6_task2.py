"""У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, 
його ім'я та вік, розділені комою. Наприклад:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота."""
cats_info = [
    "60b90c1c13067a15887e1ae1,Tayson,3",
    "60b90c2413067a15887e1ae2,Vika,1",
    "60b90c2e13067a15887e1ae3,Barsik,2",
    "60b90c3b13067a15887e1ae4,Simon,12",
    "60b90c4613067a15887e1ae5,Tessi,5"]

with open ("cats_data.txt", "w", encoding="utf-8") as file:  # Створення файлу з даними про котиків
    for entry in cats_info:
        file.write(entry + "\n")
def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as file:
            text_from_cats_data = file.read()  # Читання вмісту файлу txt
        entries = text_from_cats_data.strip().split("\n")  # Розбиваємо текст
        cats_list = []              
        for entry in entries:
            try:
                cat_id, name, age = entry.split(",")  # Розділення по комі на id котиків, імені та віку 
                cats_list.append({"id": cat_id, "name": name, "age": int(age)})  # Створення словника з інформацією про котика
            except ValueError:  
                continue 
        return cats_list
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return []
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return []
