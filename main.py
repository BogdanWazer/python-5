# Імпорт бібліотеки регулярних виразів та бібліотеки для правильного сортування слів
import re
import pyuca

# Функція для зчитування першого речення з файлу
def read_first_sentence(file_name):
    try:
        # Відкриваємо файл для читання з кодуванням utf-8
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            # Шукаємо перше речення в тексті за допомогою регулярного виразу
            match = re.search(r'[^.!?]*[.!?]', text)
            if match:
                # Виділяємо та виводимо перше речення
                first_sentence = match.group().strip()
                print("Перше речення:")
                print(first_sentence)
                return first_sentence
            else:
                # Виводимо повідомлення, якщо речень не знайдено
                print("Файл не містить речень.")
                return None
    except FileNotFoundError:
        # Виводимо повідомлення, якщо файл не знайдено
        print("Файл не знайдено.")
        return None

# Функція для виведення відсортованих слів
def print_sorted_words(sentence):
    if sentence:
        # Розділяємо речення на слова та перетворюємо їх на нижній регістр
        words = re.findall(r'\b\w+\b', sentence.lower())
        collator = pyuca.Collator()  # Створюємо об'єкт для сортування слів
        # Відбираємо слова українською та англійською мовами
        ukr_words = [word for word in words if re.match(
            r'^[А-ЯЇЄІҐа-яїєіґ\'’ё]+$', word)]
        eng_words = [word for word in words if re.match(
            r'^[a-zA-Z\'’]+$', word)]
        # Сортуємо слова українською мовою за допомогою pyuca
        ukr_words.sort(key=collator.sort_key)
        eng_words.sort()  # Сортуємо слова англійською мовою
        # Виводимо відсортовані слова та їх кількість
        print("\nСлова українською мовою:")
        print(', '.join(ukr_words))
        print("Кількість слів українською мовою:", len(ukr_words))
        print("\nСлова англійською мовою:")
        print(', '.join(eng_words))
        print("Кількість слів англійською мовою:", len(eng_words))

# Функція main для запуску програми
def main():
    file_name = 'file.txt'  # Вказуємо назву файлу, який потрібно обробити
    first_sentence = read_first_sentence(file_name)  # Зчитуємо перше речення
    print_sorted_words(first_sentence)  # Виводимо відсортовані слова

if __name__ == "__main__":
    main()  # Запускаємо головну функцію при запуску скрипту
