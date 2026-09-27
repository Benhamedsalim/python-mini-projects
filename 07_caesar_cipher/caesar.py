"""
شيفرة قيصر - تشفير وفك تشفير النصوص.
Caesar Cipher - encrypt and decrypt text.
"""

import string


ALPHABET = string.ascii_lowercase
ALPHABET_SIZE = len(ALPHABET)
WELCOME_MSG = "~~~~~~ Welcome to my App ~~~~~~"


def caesar_shift(text, shift):
    """إزاحة كل حرف في النص بمقدار shift."""
    result = ""

    for letter in text:
        if letter.lower() in ALPHABET:
            original_pos = ALPHABET.index(letter.lower())
            new_pos = (original_pos + shift) % ALPHABET_SIZE
            new_letter = ALPHABET[new_pos]

            if letter.isupper():
                new_letter = new_letter.upper()

            result += new_letter
        else:
            result += letter

    return result


def encrypt(text, shift):
    """تشفير النص."""
    return caesar_shift(text, shift)


def decrypt(text, shift):
    """فك تشفير النص."""
    return caesar_shift(text, -shift)


def get_shift():
    """قراءة قيمة الإزاحة من المستخدم."""
    while True:
        try:
            return int(input("Enter the shift number: "))
        except ValueError:
            print("❌ Please enter a valid integer.\n")


def get_mode():
    """قراءة الوضع (تشفير أو فك)."""
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
        if mode in ("e", "encrypt", "تشفير"):
            return "encrypt"
        if mode in ("d", "decrypt", "فك"):
            return "decrypt"
        print("❌ Please enter 'e' or 'd'.\n")


def main():
    print(WELCOME_MSG + "\n")

    mode = get_mode()
    text = input("Please type your text: ")
    shift = get_shift()

    if mode == "encrypt":
        result = encrypt(text, shift)
        print(f"\n🔒 Encrypted text:\n{result}")
    else:
        result = decrypt(text, shift)
        print(f"\n🔓 Decrypted text:\n{result}")


if __name__ == "__main__":
    main()