with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            letter_lines = letter.readlines()
            letter_lines[0] = letter_lines[0].replace("[name]", name.strip())
            with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as new_letter:
                for line in letter_lines:
                    new_letter.write(f"{line}")


