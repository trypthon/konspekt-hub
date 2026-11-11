"""
КонспектХаб (NoteSwap) v1.0 (MVP)
Простое приложение для обмена конспектами между студентами.
"""

import os
import sys
import time

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(message="Нажмите Enter для продолжения..."):
    """Показывает сообщение и ждёт нажатия Enter."""
    input(f"\n{Color.YELLOW}{message}{Color.RESET}")

def print_header(title):
    """Печатает красивый заголовок раздела."""
    clear_screen()
    print(f"\n{Color.BOLD}{Color.CYAN}{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}{Color.RESET}\n")

#бд
requests_db = []


def show_splash():
    """Заставка при запуске."""
    clear_screen()
    print(f"\n{Color.BOLD}{Color.CYAN}")
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║                                           ║")
    print("  ║       🎓 КОНСПЕКТХАБ v1.0 🎓              ║")
    print("  ║   Биржа конспектов и материалов           ║")
    print("  ║                                           ║")
    print("  ╚═══════════════════════════════════════════╝")
    print(f"{Color.RESET}")
    print(f"{Color.YELLOW}  Загрузка...{Color.RESET}")
    time.sleep(1.5)

def create_request():
    """Создание нового запроса с валидацией."""
    print_header("📝 СОЗДАНИЕ НОВОГО ЗАПРОСА")
    
    subject = input(f"{Color.WHITE}Введите предмет (обязательно): {Color.RESET}").strip()
    
    if not subject:
        print(f"\n{Color.RED}❌ Ошибка: Поле 'Предмет' обязательно для заполнения!{Color.RESET}")
        pause()
        return
    
    topic = input(f"{Color.WHITE}Введите тему: {Color.RESET}").strip()
    date = input(f"{Color.WHITE}Введите дату (например, 10.10): {Color.RESET}").strip()
    
    print(f"\n{Color.CYAN}Тип запроса:{Color.RESET}")
    print("  1 - Ищу конспект")
    print("  2 - Предлагаю конспект")
    req_type = input(f"{Color.WHITE}Ваш выбор (1 или 2): {Color.RESET}").strip()
    type_text = "🔍 Ищу" if req_type == "1" else "📤 Предлагаю"

    
    new_request = {
        "id": len(requests_db) + 1,
        "subject": subject,
        "topic": topic,
        "date": date,
        "type": type_text,
        "contact": "Не указан"
    }
    requests_db.append(new_request)
    
    print(f"\n{Color.GREEN}✅ Запрос #{new_request['id']} успешно создан!{Color.RESET}")
    pause()

def view_feed():
    """Просмотр ленты запросов в виде красивой таблицы."""
    print_header("📋 ЛЕНТА ЗАПРОСОВ")
    
    if not requests_db:
        print(f"{Color.YELLOW}  Лента пока пуста. Будьте первым, кто создаст запрос!{Color.RESET}")
        pause()
        return
    
    
    print(f"{Color.BOLD}{'ID':<4} {'Тип':<15} {'Предмет':<15} {'Тема':<15} {'Дата':<8} {'Контакт'}{Color.RESET}")
    print(f"{Color.CYAN}{'─' * 4} {'─' * 15} {'─' * 15} {'─' * 15} {'─' * 8} {'─' * 20}{Color.RESET}")
    
    for req in requests_db:
        contact_display = req['contact'] if req['contact'] != "Не указан" else f"{Color.YELLOW}Не указан{Color.RESET}"
        print(f"{req['id']:<4} {req['type']:<15} {req['subject']:<15} {req['topic']:<15} {req['date']:<8} {contact_display}")
    
    print()
    pause()

def leave_contact():
    """Оставление контакта под запросом."""
    print_header("📞 ОСТАВИТЬ КОНТАКТ")
    
    if not requests_db:
        print(f"{Color.YELLOW}  Лента пуста. Сначала создайте запрос!{Color.RESET}")
        pause()
        return
    
    
    print(f"{Color.BOLD}Доступные запросы:{Color.RESET}\n")
    for req in requests_db:
        print(f"  [{req['id']}] {req['type']} | {req['subject']} - {req['topic']} ({req['date']})")
    print()
    
    try:
        req_id = int(input(f"{Color.WHITE}Введите номер запроса (ID): {Color.RESET}"))
        target_req = next((req for req in requests_db if req["id"] == req_id), None)
        
        if target_req:
            new_contact = input(f"{Color.WHITE}Введите ваш контакт (например, @telegram): {Color.RESET}").strip()
            if new_contact:
                target_req["contact"] = new_contact
                print(f"\n{Color.GREEN}✅ Контакт успешно обновлён для запроса #{req_id}!{Color.RESET}")
            else:
                print(f"\n{Color.RED}❌ Контакт не может быть пустым.{Color.RESET}")
        else:
            print(f"\n{Color.RED}❌ Запрос с номером {req_id} не найден.{Color.RESET}")
    except ValueError:
        print(f"\n{Color.RED}❌ Ошибка: введите корректное число.{Color.RESET}")
    
    pause()

#глав меню
def main():
    """Главная функция приложения."""
    show_splash()
    
    while True:
        print_header("🏠 ГЛАВНОЕ МЕНЮ")
        print(f"  {Color.GREEN}1.{Color.RESET} Создать запрос на конспект")
        print(f"  {Color.GREEN}2.{Color.RESET} Просмотреть ленту запросов")
        print(f"  {Color.GREEN}3.{Color.RESET} Оставить контакт под запросом")
        print(f"  {Color.RED}0.{Color.RESET} Выход")
        print()
        
        choice = input(f"{Color.WHITE}  Ваш выбор (0-3): {Color.RESET}").strip()
        
        if choice == '1':
            create_request()
        elif choice == '2':
            view_feed()
        elif choice == '3':
            leave_contact()
        elif choice == '0':
            clear_screen()
            print(f"\n{Color.BOLD}{Color.CYAN}")
            print("  ╔═══════════════════════════════════════════╗")
            print("  ║                                           ║")
            print("  ║       👋 До свидания! Спасибо за          ║")
            print("  ║          использование КонспектХаба!      ║")
            print("  ║                                           ║")
            print("  ╚═══════════════════════════════════════════╝")
            print(f"{Color.RESET}\n")
            break
        else:
            print(f"\n{Color.RED}⚠️  Неверный ввод. Пожалуйста, выберите число от 0 до 3.{Color.RESET}")
            pause()

if __name__ == "__main__":
    main()
