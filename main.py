import sqlite3

#Database connection
connection = sqlite3.connect('student_management.db')
cursor=connection.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

#Create courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL UNIQUE)
""")

connection.commit()

# Add courses
cursor.execute(
    "INSERT OR IGNORE INTO courses (course_name) VALUES (?)",
    ("Python",)
)

cursor.execute(
    "INSERT OR IGNORE INTO courses (course_name) VALUES (?)",
    ("Java",)
)

cursor.execute(
    "INSERT OR IGNORE INTO courses (course_name) VALUES (?)",
    ("Data Science",)
)

connection.commit()

# view courses
cursor.execute("SELECT * FROM courses")
print(cursor.fetchall())

# create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    mark INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
)
""")

connection.commit()

# Add student function
def add_student():
    name=input("Enter student name: ")
    age=int(input("Enter age: "))
    course_id=int(input("Enter course ID: "))
    mark=int(input("Enter mark: "))

    cursor.execute("""
    INSERT INTO students(name,age,course_id,mark)
    VALUES(?,?,?,?)
    """,(name,age,course_id,mark))

    connection.commit()
    print("student added successfully")

# View all students
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# view students with course names
def view_students():
    cursor.execute("""
    SELECT students.name, students.age, courses.course_name, students.mark
    FROM students
    INNER JOIN courses 
    ON students.course_id = courses.id
    """)
    print(cursor.fetchall())

# Update student
def update_student():
    student_id = int(input("Enter Student ID: "))
    new_mark = int(input("Enter new mark: "))

    cursor.execute("""
    UPDATE students
    SET mark = ?
    WHERE id = ?
    """,(new_mark,student_id))

    connection.commit()
    print("Student updated successfully")

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Delete student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    cursor.execute("""
    DELETE FROM students
    WHERE id = ?
    """,(student_id,))

    connection.commit()
    print("Student deleted successfully")

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# search student
def search_student():
    name = input("Enter student name to search: ")

    cursor.execute("""
    SELECT students.name, students.age, courses.course_name, students.mark
    FROM students
    INNER JOIN courses
    ON students.course_id = courses.id
    WHERE students.name = ?
    """,(name,))

    print(cursor.fetchall())

# Main menu
def main_menu():
    while True:
        print("\n====Student Management System====")
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search student")
        print("6. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("invalid choice")

main_menu()




