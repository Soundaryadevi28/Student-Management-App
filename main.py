import mysql.connector

class StudentManagementSystem:
    def __init__(self):
        # Database Connection - Update user/password for your local MySQL
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",      
                password="yourpassword", 
                database="school_db"
            )
            self.cursor = self.db.cursor()
            print("Connected to database successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_student(self, sid, name, age, course, grade):
        try:
            sql = "INSERT INTO students (student_id, name, age, course, grade) VALUES (%s, %s, %s, %s, %s)"
            val = (sid, name, age, course, grade)
            self.cursor.execute(sql, val)
            self.db.commit()
            print(f"\nStudent {name} added successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to add student: {err}")

    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        records = self.cursor.fetchall()
        print("\n--- Current Student Records ---")
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Grade: {row[4]}")

    def delete_student(self, sid):
        sql = "DELETE FROM students WHERE student_id = %s"
        self.cursor.execute(sql, (sid,))
        self.db.commit()
        print(f"\nRecord with ID {sid} has been deleted.")

# This part makes the code interactive
if __name__ == "__main__":
    # Note: Make sure you run the SQL script in MySQL Workbench first!
    sms = StudentManagementSystem()
    
    while True:
        print("\n--- STUDENT SYSTEM MENU ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Delete a Student")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Full Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course Name: ")
            grade = input("Enter Grade (e.g., A, B, C): ")
            sms.add_student(sid, name, age, course, grade)
            
        elif choice == '2':
            sms.view_students()
            
        elif choice == '3':
            sid = input("Enter the Student ID to delete: ")
            sms.delete_student(sid)
            
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
