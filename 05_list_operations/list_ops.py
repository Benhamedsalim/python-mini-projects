"""
تمرين على القوائم في Python.
List operations practice.
"""

WELCOME_MSG = "~~~~~~ Welcome to my App ~~~~~~"


def main():
    print(WELCOME_MSG)

    print("\n--- First Basket ---")

    first_basket = [
        ["Apples", "Bananas"],
        ["Milk", "Water"],
    ]

    print(" ".join(first_basket[0]) + " " + " ".join(first_basket[1]))
    print(first_basket[0][0], first_basket[1][0])

    first_basket.append(["Cake", "Candy"])
    print("\nAfter append:")
    print(first_basket)

    first_basket.insert(0, "Salim")
    first_basket.insert(3, "book4")
    first_basket.insert(5, "book6")

    print("\nAfter inserts:")
    print(first_basket)

    print("\n--- Second Basket ---")

    second_basket = [
        ["Apples", "Bananas"],
        ["Milk", "Water"],
    ]

    input("Press Enter to update the second basket...")

    print("\nHere is the updated basket:")

    second_basket.insert(
        0,
        ["Oranges", "Apples", "Bananas", "Kiwis"],
    )

    second_basket.pop(1)
    second_basket.append([1, 2, 3])

    print(second_basket)


if __name__ == "__main__":
    main()