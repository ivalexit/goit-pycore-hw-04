def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            try:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)
            except ValueError:
                print(f"Невідповідний формат рядка: {line.strip()}")
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except Exception as e:
        print(f"Відбулась помилка: {e}")
        return []
    
    return cats

cats_info = get_cats_info("cats_info_list.txt")
print(cats_info)


