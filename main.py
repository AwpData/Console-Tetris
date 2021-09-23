import numpy as np

coords = {"I": [[4, 14, 24, 34], [3, 4, 5, 6]],
          "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]],
          "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
          "S": [[5, 4, 14, 13], [4, 14, 15, 25]],
          "Z": [[4, 5, 15, 16], [5, 15, 14, 24]],
          "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
          "O": [[4, 14, 15, 5]]}


def print_board(pos=(-1, -1, -1, -1), width=10, length=20):
    arr = np.array(["-" for i in range(length * width)])
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
            if curr_coord - 1 < 0 or (curr_coord - 1 < curr_coord - (curr_coord % 10) and curr_coord >= 10):
                ncoords[coord] = int(round(curr_coord + 5.1, -1))  # round function rounds to nearest ten
        ncoords = list(map(lambda x: (x - 1), ncoords))
    elif direction == "right":
        for coord in range(len(ncoords)):
            curr_coord = ncoords[coord]
            if str(curr_coord).endswith("9"):
                ncoords[coord] = int(round(curr_coord - 5, -1) - 1)  # round function rounds to nearest ten
        ncoords = list(map(lambda x: (x + 1), ncoords))
    elif direction == "down":
        for coord in range(len(ncoords)):
            curr_coord = ncoords[coord]
            if length * width - 10 <= curr_coord <= length * width - 1:
                ncoords[coord] = curr_coord % int(round(length * width - 10, -1))
            else:
                ncoords[coord] += 10
    return ncoords


block = input().upper()
dimensions = input().split()
width = int(dimensions[0])
length = int(dimensions[1])
base = 0
print_board((-1, -1, -1, -1), width, length)
while True:
    print_board(coords[block][base % len(coords[block])], width, length)
    command = input().lower()
    if command == "exit":
        break
    elif command == "rotate":
        base += 1  # Base = the index of the current block
    else:
        if command in ["left", "right", "down"]:
            for i in range(0, len(coords[block])):
                coords[block][i] = change_coords(command, i)
    if command != "down":
        for i in range(0, len(coords[block])):
            coords[block][i] = change_coords("down", i)
