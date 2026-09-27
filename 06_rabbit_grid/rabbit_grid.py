"""
لعبة شبكة الأرنب - ضع الأرنب في مكان محدد.
Rabbit grid game - place the rabbit at a specific position.
"""

GRID_SIZE = 3
EMPTY = "🌿"
RABBIT = "🐇"


def create_grid(size):
    """إنشاء شبكة فارغة بحجم معين."""
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def display_grid(grid):
    """عرض الشبكة."""
    for row in grid:
        print(" ".join(row))
    print()


def get_position(size):
    """قراءة إحداثيات صحيحة من المستخدم."""
    while True:
        position = input(
            f"Where do you want the rabbit? "
            f"(enter two numbers 1-{size}, e.g. 12): "
        ).strip()

        if len(position) != 2:
            print("❌ Please enter exactly 2 digits.\n")
            continue

        if not position.isdigit():
            print(f"❌ Please enter numbers only (1-{size}).\n")
            continue

        x = int(position[0])
        y = int(position[1])

        if not (1 <= x <= size and 1 <= y <= size):
            print(f"❌ Numbers must be between 1 and {size}.\n")
            continue

        return x - 1, y - 1


def main():
    print("~~~~~~ Welcome to my App ~~~~~~\n")

    grid = create_grid(GRID_SIZE)

    print("Here is the empty grid:\n")
    display_grid(grid)

    print(f"Where do you want this rabbit {RABBIT}?\n")
    x, y = get_position(GRID_SIZE)

    grid[x][y] = RABBIT

    print(f"\n🐇 Rabbit placed at ({x + 1}, {y + 1})!\n")
    display_grid(grid)


if __name__ == "__main__":
    main()