
height = None

while height is None:
    text = input("How tall should the tree be?")
    try:
        height = int(text)
        if (height < 0):
            raise("Brev")
    except:
        print("Please put in a valid height!")
        height = None

# this is the number of characters on each level
num_characters = 2 * height - 1

for depth in range(height):
    # this is the number of spaces to be printed on each side
    num_spaces = num_characters - depth * 2 - 1
    num_spaces = int(num_spaces / 2)

    # print first spaces
    for i in range(num_spaces):
        print(' ', end='', flush=True)

    # print tree
    for i in range(depth * 2 + 1):
        print('*', end='', flush=True)

    # print second spaces
    for i in range(num_spaces):
        print(' ', end='', flush=True)

    # add new line
    print()

# print the tree trunk
num_spaces = num_characters - 1
num_spaces = int(num_spaces / 2)

for i in range(num_spaces):
    print(' ', end='', flush=True)

print('|', end='', flush=True)

for i in range(num_spaces):
    print(' ', end='', flush=True)

