try:
    with open("Dungeon/Level-2/JournalSlime.txt", "r") as file:
        journal_content = file.read()

    number = int(journal_content.split(" ")[-2]) + 1 # Extract the number from the journal content and add 1

    journal_content = f"Journal Was Ran: {number} times"

except FileNotFoundError:
    journal_content = "Journal Was Ran: 1 time"

with open("Dungeon/Level-2/JournalSlime.txt", "w") as file:
    file.write(journal_content)

print(journal_content)