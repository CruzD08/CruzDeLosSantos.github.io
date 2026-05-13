# student_database.py
# A student database program using dictionaries and tuples.

def StudentDatabase(numStudents):
    """Build a student database and allow searching by student ID."""
    students = {}  # dictionary to store student data

    # input student data
    for i in range(numStudents):
        student_id = input(f'Enter student ID for student {i + 1}: ')
        name = input(f'Enter name for student {i + 1}: ')
        major = input(f'Enter major for student {i + 1}: ')
        students[student_id] = (name, major)  # store as tuple

    print(f'\n{len(students)} student(s) stored in the database.\n')

    # search loop
    while True:
        search_id = input('Enter a student ID to search (or press Enter to quit): ')

        if search_id == '':  # blank input exits
            print('Exiting the student database. Goodbye!')
            break

        if search_id in students:
            name, major = students[search_id]
            print(f'\nStudent ID: {search_id}')
            print(f'Name: {name}')
            print(f'Major: {major}\n')
        else:
            print(f'\nStudent ID "{search_id}" not found.\n')


# main program
num = int(input('How many students would you like to enter? '))
StudentDatabase(num)
