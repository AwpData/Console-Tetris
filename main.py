import numpy as np

coords = {"I": [[4, 14, 24, 34], [3, 4, 5, 6]],
          "T": [[4, 14, 15, 24], [4, 13, 14, 15], [4, 5, 6, 15], [5, 14, 15, 25]],
          "J": [[5, 15, 24, 25], [3, 4, 5, 15], [5, 4, 14, 24], [4, 14, 15, 16]],
          "S": [[5, 4, 13, 14], [4, 14, 15, 25]],
          "Z": [[4, 5, 15, 16], [5, 14, 15, 24]],
          "L": [[4, 14, 24, 25], [5, 13, 14, 15], [4, 5, 15, 25], [4, 5, 6, 14]],
          "O": [[4, 5, 14, 15]]}


def print_board(pos=(-1, -1, -1, -1), width=10, length=20):
    arr = np.array(["-" for _ in range(length * width)])
    for cell in range(0, arr.size):
        if cell in pos:
            arr[cell] = "0"
        if cell % width == 0:
            print(end="\n")
            print(arr[cell], end="")
        else:
            print(" " + arr[cell], end="")
    print(end="\n")


def change_coords(direction, index):
    ncoords = coords[block][index]
    if direction == "left":
        for coord in range(len(ncoords)):
            curr_coord = ncoords[coord]
            if curr_coord - 1 < curr_coord - (curr_coord % 10):
                break
        else:
            ncoords = list(map(lambda x: x - 1, ncoords))

    elif direction == "right":
        for coord in range(len(ncoords) - 1, -1, -1):
            curr_coord = ncoords[coord]
            if str(curr_coord).endswith("9"):
                break
        else:
            ncoords = list(map(lambda x: x + 1, ncoords))

    elif direction == "down":
        ncoords = list(map(lambda x: x + 10, ncoords))
        for coord in range(len(ncoords) - 1, -1, -1):
            curr_coord = ncoords[coord]
            if length * width - 10 <= curr_coord <= length * width - 1 and curr_coord not in occupied_spaces[i]:
                for coord in ncoords:
                    occupied_spaces[index].add(coord)
                break

    return ncoords


block = input().upper()
dimensions = input().split()
width = int(dimensions[0])
length = int(dimensions[1])
base = 0
occupied_spaces = [set(), set(), set(), set()]
print_board((-1, -1, -1, -1), width, length)
while True:
    print_board(coords[block][base % len(coords[block])], width, length)
    command = input().lower()
    if command == "exit":
        break
    elif command == "rotate":
        if coords[block][base % len(coords[block])][len(block) - 1] not in occupied_spaces[base % len(coords[block])]:
            base += 1  # Base = the index of the current block
    else:
        if command in ["left", "right", "down"] and coords[block][base % len(coords[block])][
            len(block) - 1] not in occupied_spaces[base % len(coords[block])]:
            for i in range(0, len(coords[block])):
                coords[block][i] = change_coords(command, i)
    if command != "down" and coords[block][base % len(coords[block])][len(block) - 1] not in occupied_spaces[
        base % len(coords[block])]:
        for i in range(0, len(coords[block])):
            coords[block][i] = change_coords("down", i)
