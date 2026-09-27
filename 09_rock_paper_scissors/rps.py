"""
لعبة حجر-ورق-مقص.
Rock-Paper-Scissors game.
"""

import random
import textwrap


ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
CHOICES = [ROCK, PAPER, SCISSORS]

BEATS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

ASCII_ART = {
    ROCK: textwrap.dedent("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """),
    PAPER: textwrap.dedent("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """),
    SCISSORS: textwrap.dedent("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """),
}

RULES = """
********** RULES **********
1) You choose and the computer chooses.
2) Rock smashes Scissors → Rock wins.
3) Scissors cut Paper → Scissors win.
4) Paper covers Rock → Paper wins.
"""


def show_ascii(choice):
    """عرض ASCII للاختيار."""
    print(ASCII_ART[choice])


def get_user_choice():
    """قراءة اختيار المستخدم."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()

        if choice in CHOICES:
            return choice

        print(f"❌ Invalid choice. Please choose from {CHOICES}.\n")


def get_computer_choice():
    """اختيار عشوائي للكمبيوتر."""
    return random.choice(CHOICES)


def get_winner(user, computer):
    """تحديد الفائز."""
    if user == computer:
        return "tie"
    if BEATS[user] == computer:
        return "user"
    return "computer"


def play_round():
    """جولة واحدة."""
    user_choice = get_user_choice()
    print(f"\n👤 You chose: {user_choice}")
    show_ascii(user_choice)

    computer_choice = get_computer_choice()
    print(f"🤖 Computer chose: {computer_choice}")
    show_ascii(computer_choice)

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("🤝 It's a tie!")
    elif result == "user":
        print(f"🎉 You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"💀 You lose! {computer_choice} beats {user_choice}.")

    return result


def show_score(score):
    """عرض النقاط."""
    print("\n" + "=" * 30)
    print(f"👤 You:      {score['user']}")
    print(f"🤖 Computer: {score['computer']}")
    print(f"🤝 Ties:     {score['tie']}")
    print("=" * 30)


def ask_play_again():
    """سؤال المستخدم إن كان يريد اللعب مرة أخرى."""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("❌ Please enter 'y' or 'n'.")


def main():
    print("~~~~~~ Welcome to Rock-Paper-Scissors ~~~~~~\n")

    command = input("Type 'help' for rules, or press Enter to play: ").strip().lower()

    if command == "help":
        print(RULES)

    score = {"user": 0, "computer": 0, "tie": 0}

    while True:
        result = play_round()
        score[result] += 1
        show_score(score)

        if not ask_play_again():
            break

    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()