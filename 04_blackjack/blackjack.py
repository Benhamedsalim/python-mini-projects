"""
لعبة Blackjack (Twenty One) - لعبة ورق.
Blackjack (Twenty One) game.
"""

import random
import os
import time


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21
COMPUTER_MIN_SCORE = 17

LOGO = """
 .------.            .------.
/ .----. \\          / .----. \\    _     _ _ _       _
| |  A   | |        | |  J   | |  | |   | | | | ___ | | ___
| |    ♣ | |        | |    ♠ | |  | |_  | | | |/ __|| |/ __|
| |   ♣ ♣| |        | |   ( )| |  |  _ \\ | | | | |   | |\\__ \\
\\ '----' /          \\ '----' /    | |_) || | | | |__ | | ___| |_|
 '------'            '------'     |____/ |_|_|_|\\___||_||____/(_)
"""


def clear():
    """مسح الشاشة."""
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """سحب كرت عشوائي."""
    return random.choice(CARDS)


def calculate_score(cards):
    """حساب مجموع الكروت مع معالجة الآس (11 أو 1)."""
    if sum(cards) == BLACKJACK and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > BLACKJACK:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def format_score(score):
    """عرض النتيجة (0 تعني Blackjack)."""
    return BLACKJACK if score == 0 else score


def get_yes_no(prompt):
    """قراءة نعم/لا من المستخدم."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("❌ Please enter 'y' or 'n'.")


def compare(user_score, computer_score):
    """مقارنة نتائج المستخدم والحاسوب."""
    if user_score == computer_score:
        return "🤝 Draw!"
    if user_score > BLACKJACK:
        return "💀 You went over 21. Sorry!"
    if computer_score > BLACKJACK:
        return "🏆 Computer went over 21. You win!"
    if user_score == 0:
        return "🥇🥇🥇 Blackjack! You win!"
    if computer_score == 0:
        return "😢 Computer had a Blackjack. You lose!"
    if user_score > computer_score:
        return "👌 You win!"
    return "😢 You lose!"


def play_blackjack():
    """تشغيل جولة من Blackjack."""
    clear()
    print(LOGO)
    print("Starting game...")
    time.sleep(1.5)
    clear()

    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n🃏 Your cards: {user_cards}  →  Score: {format_score(user_score)}")
        print(f"🤖 Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 \
                or user_score > BLACKJACK or computer_score > BLACKJACK:
            game_continue = False
        elif get_yes_no("Get another card? (y/n): "):
            user_cards.append(deal_card())
        else:
            game_continue = False

    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < COMPUTER_MIN_SCORE:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n" + "=" * 40)
    print(f"🃏 Your final hand: {user_cards}  →  Score: {format_score(user_score)}")
    print(f"🤖 Computer's final hand: {computer_cards}  →  Score: {format_score(computer_score)}")
    print("=" * 40)
    print(compare(user_score, computer_score))
    print("=" * 40)


def show_menu():
    """عرض القائمة الرئيسية."""
    print("\n" + "=" * 40)
    print("🎮 Choose a game:")
    print("=" * 40)
    print("1. Blackjack (Twenty One)")
    print("2. Exit")
    print("=" * 40)


def main():
    """نقطة الدخول."""
    print("~~~~~~ Welcome to my App ~~~~~~")

    while True:
        show_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            play_blackjack()
        elif choice == "2":
            print("👋 Thanks for playing! See you next time.")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()