import random
import os


MAX_COL = 6
MAX_ROW = 6

game = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def machine_random():
    row = random.randint(0, MAX_ROW - 1)
    return row


def change_item_special(col: int, row: int):
    global game
    if game[col][row] == "o":
        return

    if game[col][row] == "x":
        game[col][row] = "🅧"
        return

    if game[col][row] == "w":
        game[col][row] = "🅦"
        return


def check_col(col: int, row: int):
    global game

    if row > MAX_ROW - 3:
        return

    if game[col][row] == "o":
        return

    if game[col][row] == game[col][row + 1] == game[col][row + 2]:
        clear_screen()
        print("{} win 👑!! col".format(game[col][row]))

        for i in range(3):
            change_item_special(col, row + i)
        print_game()
        exit()


def check_row(col: int, row: int):
    global game

    if col > MAX_COL - 3:
        return

    if game[col][row] == "o":
        return

    if game[col][row] == game[col + 1][row] == game[col + 2][row]:
        clear_screen()
        print("{} win 👑!! row".format(game[col][row]))
        for i in range(3):
            change_item_special(col + i, row)
        print_game()
        exit()


#     /
#   /
# /
def check_cross_down_left_to_right_up(col: int, row: int):
    global game
    if row < MAX_COL - 4 or col > MAX_COL - 2:
        return

    if game[col][row] == "o":
        return

    if game[col][row] == game[col - 1][row - 1] == game[col - 2][row - 2]:
        clear_screen()
        print("{} win 👑!! cross".format(game[col][row]))
        for i in range(3):
            change_item_special(col - i, row - i)
        print_game()
        exit()

    return


# \
#   \
#     \
def check_cross_up_left_to_right_down(col: int, row: int):
    if col > MAX_COL - 3 or row > MAX_ROW - 3:
        return

    if game[col][row] == "o":
        return

    if game[col][row] == game[col + 1][row + 1] == game[col + 2][row + 2]:
        clear_screen()
        print("{} win 👑!! cross".format(game[col][row]))
        for i in range(3):
            change_item_special(col + 1, row + 1)
        print_game()
        exit()


def check_game():
    for col in range(MAX_COL):
        for row in range(MAX_ROW):
            check_col(col, row)
            check_row(col, row)
            check_cross_down_left_to_right_up(col, row)
            check_cross_up_left_to_right_down(col, row)


def print_game():
    for row in range(MAX_ROW):
        for col in range(MAX_COL):
            print("{}".format(game[col][row]), end="|")
        print()


def clear_game():
    global game

    game = []
    for col in range(MAX_COL):
        game.append([])

        for _ in range(MAX_ROW):
            game[col].append("o")


def drop_item(col: int, item: str):
    for row in range(MAX_ROW - 1, -1, -1):
        if game[col][row] != "o":
            continue

        game[col][row] = item
        return


if __name__ == "__main__":
    bot_enable = True

    clear_game()
    clear_screen()

    while True:
        if bot_enable:
            drop_item(machine_random(), "w")
        check_game()
        print_game()

        user_input = str(input("Enter slot (1-{}) : ".format(MAX_ROW)))
        if user_input in ["q", "exit"]:
            break

        if user_input in ["c", "clear"]:
            clear_game()
            clear_screen()
            continue

        if user_input == "b":
            bot_enable = not bot_enable
            if bot_enable:
                print("Bot enable successful!✅")
            else:
                print("Bot disable successful!⛔️")

            continue

        if not user_input.isnumeric():
            print("input invalid")
            continue

        n = abs(int(user_input))

        if n < 1 or n > MAX_ROW:
            print("wrong input!")
            continue

        n = n - 1

        drop_item(n, "x")
