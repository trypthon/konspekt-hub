"""
КонспектХаб (NoteSwap) v1.0 (MVP)
Простое приложение для обмена конспектами между студентами.
"""

# Хранилище запросов (в памяти текущей сессии)
requests_db = []

def create_request():
    print("\n--- Создание нового запроса ---")
    subject = input("Введите предмет (обязательно): ").strip()
    
    # Валидация из Занятия 17
    if not subject:
        print("❌ Ошибка: Поле 'Предмет' обязательно для заполнения!")
        print("Возврат в главное меню.\n")
        return
    
    topic = input("Введите тему: ").strip()
    date = input("Введите дату (например, 10.10): ").strip()
    req_type = input("Тип (1 - Ищу, 2 - Предлагаю): ").strip()
    type_text = "Ищу" if req_type == "1" else "Предлагаю"
    
    # Сохраняем запрос
    new_request = {
        "id": len(requests_db) + 1,
        "subject": subject,
        "topic": topic,
        "date": date,
        "type": type_text,
        "contact": "Контакт не указан"
    }
    requests_db.append(new_request)
    print(f"✅ Запрос #{new_request['id']} успешно создан!\n")

def view_feed():
    print("\n--- Лента запросов ---")
    if not requests_db:
        print("Лента пока пуста. Будьте первым, кто создаст запрос!")
    else:
        for req in requests_db:
            print(f"[{req['id']}] {req['type']} | {req['subject']} | {req['topic']} ({req['date']})")
            print(f"    Контакт для связи: {req['contact']}")
            print("-" * 40)
    print()

def leave_contact():
    print("\n--- Оставить контакт ---")
    view_feed()
    if not requests_db:
        return
        
    try:
        req_id = int(input("Введите номер запроса (ID), чтобы оставить контакт: "))
        # Ищем запрос по ID
        target_req = next((req for req in requests_db if req["id"] == req_id), None)
        
        if target_req:
            new_contact = input(f"Введите ваш контакт (например, @telegram) для запроса #{req_id}: ").strip()
            if new_contact:
                target_req["contact"] = new_contact
                print("✅ Контакт успешно обновлен!\n")
            else:
                print("❌ Контакт не может быть пустым.\n")
        else:
            print("❌ Запрос с таким номером не найден.\n")
    except ValueError:
        print("❌ Ошибка: введите корректный числовой ID.\n")

def main():
    """Главная функция приложения."""
    while True:
        print("=" * 50)
        print(" 🎓 КонспектХаб — биржа конспектов и материалов")
        print("=" * 50)
        print("\nМеню:")
        print("1. Создать запрос на конспект")
        print("2. Просмотреть ленту запросов")
        print("3. Оставить контакт под запросом")
        print("0. Выход")
        
        choice = input("\nВыберите действие (0-3): ").strip()
        
        if choice == '1':
            create_request()
        elif choice == '2':
            view_feed()
        elif choice == '3':
            leave_contact()
        elif choice == '0':
            print("\n👋 До свидания! Спасибо за использование КонспектХаба.\n")
            break
        else:
            print("\n⚠️ Неверный ввод. Пожалуйста, выберите число от 0 до 3.\n")

if __name__ == "__main__":
    main()
