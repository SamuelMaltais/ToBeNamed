import csv




def getPopulationPerHood():

    # TODO be adapted to pull from https://donnees.montreal.ca/dataset/population-recensement/resource/8dbac698-14c6-4c91-9ba8-85fdb3232c45

    
    with open('employee_birthday.txt') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1

    print(f'Processed {line_count} lines.')

    # TODO
    # You can return here the object with the intended format which is gonna look like
    return

