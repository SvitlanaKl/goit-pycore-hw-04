# розробити функцію total_salary(path), яка аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників.
# Функція повинна точно обчислювати загальну та середню суми.
# Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
# Код має бути чистим, добре структурованим і зрозумілим.

def total_salary (file_path: str) -> list[int]:
    total = 0
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                surname, salary_str = line.strip().split(',') # виводимо через кому прізвище і зарплату
                salary = int(salary_str) # перетворюємо зарплату на число
                total += salary # плюсуємо до результату
                count += 1 # наступний розробник
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print("Помилка при обробці файлу:", e)
        return None, None
    # середня зарплата в межах поточної обробки файлу
    if count == 0:
        average = 0
    else:
        average = total / count
    return total, average
      
    
total, average = total_salary("HW-04_part1/salary_details.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")