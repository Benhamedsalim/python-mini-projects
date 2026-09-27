"""
مولّد كلمات مرور قوية.
Strong password generator.
"""

import string
import random


LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation


def get_positive_int(prompt, allow_zero=False):
    """قراءة عدد صحيح موجب من المستخدم."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("❌ Please enter a positive number.\n")
            elif value == 0 and not allow_zero:
                print("❌ Please enter a number greater than 0.\n")
            else:
                return value
        except ValueError:
            print("❌ Please enter a valid integer.\n")


def validate_inputs(length, letters, numbers, symbols):
    """التحقق من صحة المدخلات."""
    total = letters + numbers + symbols

    if total != length:
        print(f"❌ Sum ({total}) doesn't match length ({length}).\n")
        return False

    if total == 0:
        print("❌ Password cannot be empty.\n")
        return False

    return True


def generate_password(num_letters, num_numbers, num_symbols):
    """توليد كلمة مرور عشوائية."""
    chars = (
        random.choices(LETTERS, k=num_letters)
        + random.choices(NUMBERS, k=num_numbers)
        + random.choices(SYMBOLS, k=num_symbols)
    )

    random.shuffle(chars)
    return "".join(chars)


def main():
    print("~~~~~~ Welcome to Password Generator ~~~~~~\n")

    while True:
        length = get_positive_int("Enter the total number of characters: ")
        num_letters = get_positive_int("Enter the number of letters: ", allow_zero=True)
        num_numbers = get_positive_int("Enter the number of numbers: ", allow_zero=True)
        num_symbols = get_positive_int("Enter the number of symbols: ", allow_zero=True)

        if validate_inputs(length, num_letters, num_numbers, num_symbols):
            break
        print("Let's try again.\n")

    password = generate_password(num_letters, num_numbers, num_symbols)

    print(f"\n🔐 Generated Password: {password}")
    print(f"📏 Length: {len(password)}")


if __name__ == "__main__":
    main()