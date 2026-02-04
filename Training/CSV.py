import csv

print("My Pals:")

with open("Training/Data.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]} > {row[1]}")