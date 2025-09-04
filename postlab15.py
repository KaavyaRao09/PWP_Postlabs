import sqlite3

# Establish connection and cursor
conn = sqlite3.connect('student_record.db')
cur = conn.cursor()

# Create the student_record table if missing
cur.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    PRIMARY KEY (Enrollment, Subject)
                )''')
conn.commit()

# Get new student info and subjects with marks
enrollment = int(input("Enter Enrollment number: "))
student_name = input("Enter student name: ")
subject_total = int(input("How many subjects to enroll? "))

records = []
for i in range(subject_total):
    subj = input(f"Enter subject #{i+1}: ")
    mark_val = int(input(f"Enter mark for {subj}: "))
    records.append((enrollment, student_name, subj, mark_val))

# Insert or replace student records
cur.executemany('''INSERT OR REPLACE INTO student_record 
                   (Enrollment, name, Subject, Mark) 
                   VALUES (?, ?, ?, ?)''', records)
conn.commit()
print("\nStudent data inserted successfully.\n")

# Retrieve and show all records
cur.execute('SELECT * FROM student_record')
all_rows = cur.fetchall()
print("All Student Records:")
for r in all_rows:
    print(r)

# Query for students with marks > 90
cur.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > 90')
high_scorers = cur.fetchall()
print("\nStudents with Marks greater than 90:")
for hs in high_scorers:
    print(hs)

# Update a student's mark
update_student = input("\nEnter name to update marks: ")
update_subject = input("Enter subject to update: ")
updated_mark = int(input("Enter new mark: "))
cur.execute('''UPDATE student_record 
               SET Mark = ? 
               WHERE name = ? AND Subject = ?''', (updated_mark, update_student, update_subject))
conn.commit()
print(f"{update_student}'s mark in {update_subject} updated to {updated_mark}.")

# Delete student record(s)
delete_student = input("\nEnter name to delete from records: ")
cur.execute('DELETE FROM student_record WHERE name = ?', (delete_student,))
conn.commit()

# Confirm deletion
cur.execute('SELECT * FROM student_record WHERE name = ?', (delete_student,))
if cur.fetchone() is None:
    print(f"{delete_student} has been successfully deleted.")

# Calculate and print average mark
cur.execute('SELECT AVG(Mark) FROM student_record')
avg = cur.fetchone()[0]
print(f"\nThe average mark of all students is: {avg:.2f}")

# Close database connection
conn.close()
