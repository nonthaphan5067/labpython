MAX_ROW = 10
MAX_COL = 10

MAX_MINE = 5
MINE_CHARACTER = "*"

USER_INPUT_NUMBER_OF_MINE_TITLE = "Enter Number of Mine"
USER_INPUT_LOCATION_TITLE = "Enter {} Location [Row,Col]"  # use {} for number format
USER_INPUT_LOCATION_INVALID_MESSAGE = (
    "Mine {} location invalid!"  # use {} for location number format
)

MINE_POSITION_ROW_INDEX = 0
MINE_POSITION_COL_INDEX = 1

def create_mine_grid(mine_locations: list[tuple[int, int]]):
    # craete empty grid with 0
    grid: list[list[str]] = [["0"] * MAX_COL for _ in range(MAX_ROW)]

    for mine in mine_locations:
        row, col = mine
        grid[row - 1][col - 1] = "x"

    # Update the grid with minimum distance to the closest bomb
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            if grid[i][j] != "x":
                # Calculate the minimum distance from all bomb positions
                min_distance = float("inf")
                for mine in mine_locations:
                    # print("mine", mine)
                    bomb_row, bomb_col = mine
                    distance = abs(bomb_row - 1 - i) + abs(bomb_col - 1 - j)
                    min_distance = min(min_distance, distance)
                    # print("min distance", min_distance)
                grid[i][j] = str(min_distance)

    return grid


def print_mine_grid(grid: list[list[str]]):
    # for row in range(MAX_ROW):
    #     for col in range(MAX_COL):
    #         if len(mine_positions) == 0:
    #             print(". ", end="")
    #         else:
    #             for mine_position in mine_positions:
    #                 if (
    #                     mine_position[MINE_POSITION_ROW_INDEX] == row
    #                     and mine_position[MINE_POSITION_COL_INDEX] == col
    #                 ):
    #                     print("{} ".format(MINE_CHARACTER), end="")
    #                 else:
    #                     print(". ", end="")
    #     print()
    for row in grid:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    mine_count: int = 0
    mine_locations: list[tuple[int, int]] = []

    while True:
        mine_count_char = str(input("{} ".format(USER_INPUT_NUMBER_OF_MINE_TITLE)))
        if not mine_count_char.isnumeric():
            print("Number invalid, try again!")
            continue

        mine_count = abs(int(mine_count_char))
        if mine_count > MAX_MINE:
            mine_count = 0
            print("Mine shoud below {}, try again!".format(MAX_MINE))
            continue

        mine_location_index = 0
        while True:
            if mine_location_index == mine_count:
                break

            mine_location_char = str(
                input(
                    "{} ".format(
                        USER_INPUT_LOCATION_TITLE.format(mine_location_index + 1)
                    )
                )
            )
            mine_location_split = mine_location_char.split(" ")
            # print('mine location split', mine_location_split)
            if len(mine_location_split) != 2:
                print(
                    USER_INPUT_LOCATION_INVALID_MESSAGE.format(mine_location_index + 1)
                )
                continue

            row, col = mine_location_split
            if not row.isnumeric() or not col.isnumeric():
                print(
                    USER_INPUT_LOCATION_INVALID_MESSAGE.format(mine_location_index + 1)
                )
                continue

            row, col = abs(int(row)), abs(int(col))
            if row > MAX_ROW or col > MAX_COL:
                print(
                    USER_INPUT_LOCATION_INVALID_MESSAGE.format(mine_location_index + 1)
                )
                continue

            mine_locations.append((row, col))
            mine_location_index = mine_location_index + 1

        print(mine_locations)

        break

    grid = create_mine_grid(mine_locations)
    print_mine_grid(grid)
    # print_mine_grid(`mine_positions`)
