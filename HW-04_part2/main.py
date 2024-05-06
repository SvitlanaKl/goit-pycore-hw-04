# текстовий файл містить інформацію про котів.
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
# Розробити функцію get_cats_info(path), яка читає файл та повертає список словників з інформацією про кожного кота.

def get_cats_info (file_path):
    cats_info = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при обробці файлу. {str(e)}")
    return cats_info

cats_info = get_cats_info("HW-04_part2/cats_file.txt")
print(cats_info)