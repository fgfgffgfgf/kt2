import os

HANGMAN_DIR = "hangman_stages"
os.makedirs(HANGMAN_DIR, exist_ok=True)

stages = {
    0: """   _______
   |/
   |
   |
   |
   |
   |
   |
   |
___|________""",

    1: """   _______
   |/
   |     ( )
   |
   |
   |
   |
   |
   |
___|________""",

    2: """   _______
   |/
   |     ( )
   |      |
   |
   |
   |
   |
   |
___|________""",

    3: """   _______
   |/
   |     ( )
   |     /|
   |
   |
   |
   |
   |
___|________""",

    4: """   _______
   |/
   |     ( )
   |     /|\\
   |
   |
   |
   |
   |
___|________""",

    5: """   _______
   |/
   |     ( )
   |     /|\\
   |      |
   |
   |
   |
   |
___|________""",

    6: """   _______
   |/
   |     ( )
   |     /|\\
   |      |
   |     /
   |
   |
   |
___|________""",

    7: """   _______
   |/
   |     ( )
   |     /|\\
   |      |
   |     / \\
   |
   |
   |
___|________""",
}

for num, content in stages.items():
    filepath = os.path.join(HANGMAN_DIR, f"stage_{num}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Готово!")
