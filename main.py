import re
import pyuca


def read_first_sentence(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            match = re.search(r'[^.!?]*[.!?]', text)
            if match:
                first_sentence = match.group().strip()
                print("Перше речення:")
                print(first_sentence)
                return first_sentence
            else:
                print("Файл не містить речень.")
                return None
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None


def print_sorted_words(sentence):
    if sentence:
        words = re.findall(r'\b\w+\b', sentence.lower())
        collator = pyuca.Collator()
        ukr_words = [word for word in words if re.match(
            r'^[А-ЯЇЄІҐа-яїєіґ\'’ё]+$', word)]
        eng_words = [word for word in words if re.match(
            r'^[a-zA-Z\'’]+$', word)]
        ukr_words.sort(key=collator.sort_key)
        eng_words.sort()
        print("\nСлова українською мовою:")
        print(', '.join(ukr_words))
        print("Кількість слів українською мовою:", len(ukr_words))
        print("\nСлова англійською мовою:")
        print(', '.join(eng_words))
        print("Кількість слів англійською мовою:", len(eng_words))


def main():
    file_name = 'file.txt'
    first_sentence = read_first_sentence(file_name)
    print_sorted_words(first_sentence)


if __name__ == "__main__":
    main()
