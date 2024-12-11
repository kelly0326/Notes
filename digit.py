def print_horizontal(n):
    print("-" * n)

print_horizontal(8)

def vertical_left(n):
    for i in range(n):
        print("|")

vertical_left(3)

def vertical_right(n):
    for i in range(n):
        print(" " * 8 + "|")

vertical_right(2)

def print_vertical(n, direction):
    for i in range(n):
        if direction == "R":
            print(" " * 8 + "|")
        elif direction == "L":
            print("|")
        elif direction == "B":
            print("|" + " " * 7 + "|")

def print_zero():
    print_horizontal(8)
    print_vertical(6, "B")
    print_horizontal(8)

print_zero()

def print_one():
    print_vertical(6, "R")

print_one()

def print_two():
    print_horizontal(8)
    print_vertical(3, "R")
    print_horizontal(8)
    print_vertical(3, "L")
    print_horizontal(8)

print_two()