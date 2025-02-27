import json

FILE_NAME = 'users_data.json'

def load_data():
    """Загружает данные из файла, если файл существует"""
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(users_info):
    """Сохраняет список пользователей в файл"""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(users_info, file, ensure_ascii=False, indent=4)


