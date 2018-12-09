from prims import prims

# program welcome message
print(f"This program outputs the minimum weight spanning tree.")
print(f"Hello User! Please follow the prompts below\n")


def promptUser():
    # prompt user
    file_name = input("Enter your file's name: ")
    print(f"\n")  # line break

    # prompt user
    start = int(input("Enter your starting point: [int] "))
    print(f"\n")  # line break

    # prompt user
    draw_input = input("Would you like to draw the graph? [yes/no] ")
    draw = False
    # check the user's input and assign it to the draw variable
    draw = True if draw_input == "yes" else False
    print(f"\n")  # line break

    # Call prims function and print the cost
    print(f"Cost is: {prims(file_name, start, draw)}")


if __name__ == "__main__":
    promptUser()
