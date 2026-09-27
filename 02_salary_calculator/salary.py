"""
برنامج حساب الراتب بعد الضريبة.
Salary calculator after tax.
"""

import time


TAX_RATE = 0.15
SLEEP_TIME = 1


def calculate_tax(base_salary, bonus):
    """حساب الراتب بعد الضريبة."""
    total = base_salary + bonus
    return total * (1 - TAX_RATE)


def show_salary(base_salary, bonus):
    """عرض الراتب النهائي."""
    final_salary = calculate_tax(base_salary, bonus)
    print(f"Final Salary after tax: {final_salary:.2f}")


def get_float(prompt):
    """قراءة رقم عشري مع حماية من الأخطاء."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    base_salary = get_float("Enter your base salary: ")
    bonus = get_float("How much bonus did you get: ")

    time.sleep(SLEEP_TIME)
    print("Calculating your total salary... please wait")
    time.sleep(SLEEP_TIME)
    print("Finding the tax amount in Egypt... please wait")
    time.sleep(SLEEP_TIME)
    print("Calculating your final salary... wait")

    show_salary(base_salary, bonus)


if __name__ == "__main__":
    main()