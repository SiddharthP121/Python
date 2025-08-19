import csv

with open('Users.csv', 'r') as csvFile:
    file = csv.reader(csvFile)
    header = next(file)
    for row in file:
        if len(row[1]) == 10 and '@' in row[2] and '.' in row[2]:
            at_index = row[2].find('@')
            dot_index = row[2].find('.', at_index, len(row[2]))
            if at_index < dot_index:
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]} -> Valid Record")
        else:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]} -> Invalid Record")



        