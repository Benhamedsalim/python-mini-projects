"""
لعبة Hangman - تخمين الكلمات.
Hangman game - word guessing.
"""

import random


HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
      /O   |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
      /O\  |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
      /O\  |
       |   |
      /    |
           |
     =========
    """,
    """
       +---+
       |   |
      /O\  |
       |   |
      / \  |
           |
     =========
    """,
]

WORDS = ["python", "django", "odoo", "programming", "developer", "keyboard"]

MAX_LIVES = 6


def display_word(secret_word, guessed_letters):
    """عرض الكلمة مع إخفاء الحروف غير المخمّنة."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def get_valid_guess(guessed_letters):
    """قراءة حرف صحيح من المستخدم."""
    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("❌ Please enter exactly ONE letter.\n")
            continue

        if not guess.isalpha():
            print("❌ Please enter a letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another.\n")
            continue

        return guess


def play():
    """تشغيل اللعبة."""
    print("~~~~~~ Welcome to Hangman ~~~~~~\n")

    secret_word = random.choice(WORDS)
    guessed_letters = set()
    lives = MAX_LIVES

    while lives > 0:
        print(HANGMAN_STAGES[MAX_LIVES - lives])
        print(display_word(secret_word, guessed_letters))
        print(f"❤️  Lives: {lives}")
        print(f"📝 Guessed: {', '.join(sorted(guessed_letters)) or '-'}\n")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 You win! The word was: {secret_word}")
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good! '{guess}' is in the word.\n")
        else:
            lives -= 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")

    print(HANGMAN_STAGES[-1])
    print(f"💀 You lose! The word was: {secret_word}")


if __name__ == "__main__":
    play()