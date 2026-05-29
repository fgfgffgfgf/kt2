import random
import os

WORDS_FILE = "words.txt"
HANGMAN_DIR = "hangman_stages"

def load_words():
    words = []
    descriptions = {}
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and "|" in line:
                    word, desc = line.split("|", 1)
                    words.append(word.lower())
                    descriptions[word.lower()] = desc
    if not words:
        words = ["компьютер", "программа", "алгоритм"]
        descriptions = {w: "Слово из IT" for w in words}
    return words, descriptions

def get_random_word(words):
    return random.choice(words)

def get_description(word, descriptions):
    return descriptions.get(word, "Отгадайте слово")

def load_hangman_stage(stage_num):
    filepath = os.path.join(HANGMAN_DIR, f"stage_{stage_num}.txt")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    stages = {
        0: "\n   _______\n   |/\n   |\n   |\n   |\n   |\n   |\n   |\n___|________",
        1: "\n   _______\n   |/\n   |     ( )\n   |\n   |\n   |\n   |\n   |\n___|________",
        2: "\n   _______\n   |/\n   |     ( )\n   |      |\n   |\n   |\n   |\n   |\n___|________",
        3: "\n   _______\n   |/\n   |     ( )\n   |     /|\n   |\n   |\n   |\n   |\n___|________",
        4: "\n   _______\n   |/\n   |     ( )\n   |     /|\\\n   |\n   |\n   |\n   |\n___|________",
        5: "\n   _______\n   |/\n   |     ( )\n   |     /|\\\n   |      |\n   |\n   |\n   |\n___|________",
        6: "\n   _______\n   |/\n   |     ( )\n   |     /|\\\n   |      |\n   |     /\n   |\n   |\n___|________",
        7: "\n   _______\n   |/\n   |     ( )\n   |     /|\\\n   |      |\n   |     / \\\n   |\n   |\n___|________",
    }
    return stages.get(stage_num, stages[7])

def create_display(word, guessed):
    result = []
    for letter in word:
        if letter in guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

def is_won(word, guessed):
    for letter in word:
        if letter not in guessed:
            return False
    return True

def is_lost(wrong_count):
    return wrong_count >= 7

def update_guessed(guessed, letter):
    new_set = set()
    for l in guessed:
        new_set.add(l)
    new_set.add(letter)
    return new_set

def is_valid_input(letter, guessed):
    if len(letter) != 1:
        return False
    if not letter.isalpha():
        return False
    if letter in guessed:
        return False
    return True

def count_wrong(guessed, word):
    wrong = 0
    for letter in guessed:
        if letter not in word:
            wrong = wrong + 1
    return wrong

def print_msg(msg):
    print(msg)

def print_hangman(stage_num):
    art = load_hangman_stage(stage_num)
    print(art)

def print_word(display):
    print(f"\nСлово: {display}")

def print_guessed(guessed):
    if guessed:
        letters = []
        for l in guessed:
            letters.append(l)
        letters.sort()
        print(f"Буквы: {', '.join(letters)}")
    else:
        print("Буквы: нет")

def print_game_state(display, guessed, wrong):
    print_hangman(wrong)
    print_word(display)
    print_guessed(guessed)
    print(f"Ошибок: {wrong}/7")

def get_input():
    return input("\nВведите букву: ").lower().strip()

def print_rules():
    rules = "========== ВИСЕЛИЦА ==========\nУгадайте слово по буквам\n7 ошибок = проигрыш\n================================="
    print_msg(rules)

def print_result(won, word, desc):
    if won:
        print_msg(f"\nПОБЕДА! Слово: {word} - {desc}")
    else:
        print_msg(f"\nПОРАЖЕНИЕ! Слово: {word} - {desc}")

def play_game():
    words, descs = load_words()
    word = get_random_word(words)
    description = get_description(word, descs)
    
    guessed = set()
    wrong = 0
    
    print_rules()
    
    while True:
        display = create_display(word, guessed)
        print_game_state(display, guessed, wrong)
        
        if is_won(word, guessed):
            print_result(True, word, description)
            break
        
        if is_lost(wrong):
            print_hangman(wrong)
            print_word(create_display(word, guessed))
            print_result(False, word, description)
            break
        
        letter = get_input()
        
        if not is_valid_input(letter, guessed):
            print_msg("Ошибка! Введите одну новую букву")
            continue
        
        guessed = update_guessed(guessed, letter)
        
        if letter in word:
            print_msg(f"Да! Буква {letter} есть в слове")
        else:
            wrong = wrong + 1
            print_msg(f"Нет! Буквы {letter} нет в слове")
        
        print_msg("-" * 30)
    
    print_msg("\nИгра окончена!")
