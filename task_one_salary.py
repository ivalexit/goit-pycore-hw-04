def total_salary(path):                   #функція приймає 1 аргумент path
    try: 
        with open(path, 'r', encoding='utf-8') as file:  #безпечне відкриття 
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            try:
                name, salary = line.strip().split(',')  
                total += int(salary)                   #обчислення загальної зп
                count += 1
            except ValueError:                         #обробка виключення
                print(f"Невідповідний формат рядка: {line.strip()}")

        average = total / count if count != 0 else 0     #обчислення середньої зп
        return total, average
    except FileNotFoundError:                             #обробка виключення
        print("Файл не знайдено")
        return 0, 0
    except Exception as e:
        print(f"Сталась помилка {e}")
        return 0, 0
    
total, average = total_salary("salary_file_text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    