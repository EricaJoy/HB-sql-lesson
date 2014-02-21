import sqlite3

DB = None
CONN = None

### DB QUERY FUNCTIONS ###

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

# Add a student
def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github)) # Is there any situation where DB.execute doesn't take a tuple?
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

# Query for projects by title
def project_by_title():
    pass

# Add a project
def add_a_project():
    pass

# Query for a student's grade given a project
def student_grade_by_project():
    pass

# Give a grade to a student
def give_student_grade():
    pass

# Show all the grades for a student
def show_all_student_grades():
    pass


### END DB QUERY FUNCTIONS ###

### Connect to the database ###
def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

### End connect to the database ###

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        # TODO around here somewhere: Echo user input back, ask if it looks good
        # then commit if they say yes. Then balete lines 17-18.

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

    CONN.close()

if __name__ == "__main__":
    main()
