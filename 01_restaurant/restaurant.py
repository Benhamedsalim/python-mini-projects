"""
برنامج استقبال طلب في مطعم.
Restaurant ordering program.
"""


WELCOME_MSG = "~~~~~~ Welcome to my App ~~~~~~"


def take_order(name):
    """استقبال طلب العميل."""
    print(f"Welcome to the restaurant, {name}!")
    print("Order taken successfully")
    thank_customer(name)


def thank_customer(name):
    """شكر العميل."""
    print(f"Thank you, {name}, for choosing our restaurant!")


def main():
    print(WELCOME_MSG)
    customer_name = input("What is your name? ").strip()

    if not customer_name:
        print("Name cannot be empty.")
        return

    take_order(customer_name)
    print("=" * 22)


if __name__ == "__main__":
    main()