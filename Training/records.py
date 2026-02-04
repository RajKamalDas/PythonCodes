records = []
polarity = -1


def save():
    with open("Training/Students.txt", "w") as f:
        for each in records:
            f.write(f"{each[0]}, {each[1]}, {each[2]}\n")


def load():
    try:
        with open("Training/Students.txt", "r") as f:
            for line in f.readlines():
                id, name, course = line[:-1].split(", ")
                records.append((id, name, course))
    except FileNotFoundError:
        pass


def addstudent():
    global records

    id = input("The ID:")
    name = input("The Student Name:")
    course = input("The Course:")
    student = (id, name, course)
    records.append(student)


def display():
    for student in records:
        print(f"{student[0]} : {student[1]:<15s} of {student[2]}")


def update():
    x = input("Student ID:")
    index = -1
    for student in records:
        if student[0] == x:
            index = records.index(student)
    if index != -1:
        name = input("New Name[Leave empty to keep old name]:")
        course = input("New Course[Leave empty to keep old course]:")
        id = records[index][0]
        name = records[index][1] if name == "" else name
        course = records[index][2] if course == "" else course
        records.pop(index)
        records.insert(index, (id, name, course))
    else:
        print("Student record not found.")


def delete():
    x = input("Student ID:")
    index = -1
    for student in records:
        if student[0] == x:
            index = records.index(student)
    if index != -1:
        records.pop(index)
        print("Student record deleted.")
    else:
        print("Student record not found.")


def sort():
    global polarity
    x = input(
        """Select the order:
              1) ID
              2) Name
              3) Course
             :"""
    )
    x = int(x) - 1
    for i in range(len(records)):
        for j in range(i, len(records)):
            if polarity != x:
                if records[i][x] > records[j][x]:
                    records[i], records[j] = records[j], records[i]
            else:
                if records[i][x] < records[j][x]:
                    records[i], records[j] = records[j], records[i]
    polarity = x if polarity != x else -1


def run():
    runner = True
    load()
    while runner:
        print(
            """What would you like to do?
            1) Add a Record
            2) Display Records
            3) Update a Record
            4) Delete a Record
            5) Reorder Records
            6) Exit"""
        )
        try:
            x = int(input("Your Choice:"))
        except ValueError:
            x = 5
        match x:
            case 1:
                addstudent()
            case 2:
                display()
            case 3:
                update()
            case 4:
                delete()
            case 5:
                sort()
            case 6:
                runner = False
    save()


run()
