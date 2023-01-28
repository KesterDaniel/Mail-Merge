with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    full_letter = letter.read()
    for name in names:
        new_letter = full_letter.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)


