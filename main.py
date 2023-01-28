with open("./Input/Letters/starting_letter.txt") as letter:
    letter_lines = letter.readlines()
    with open("./Input/Names/invited_names.txt") as invited_names:
        names = invited_names.readlines()
        for name in names:
            letter_lines[0].replace("[name]", f"{name}")
            







# for line in letter_lines:
    #     print(f"{line}")
    # # print(letter_lines[0].replace("[name]", "Me"))