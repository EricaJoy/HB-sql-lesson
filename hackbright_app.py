import sqlite3

DB = None
CONN = None

### schema ###

# This is just here for reference while writing queries

# CREATE TABLE Grades (student_github varchar(30), project_title varchar(30), grade INT);
# CREATE TABLE Projects (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(30), description TEXT, max_grade INT);
# CREATE TABLE Students (first_name varchar(30), last_name varchar(30), github varchar(30));
### end schema ###



### DB QUERY FUNCTIONS ###

### ** DB WRITES ** ### 

# Add a student
def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github)) # Is there any situation where DB.execute doesn't take a tuple?
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

# Add a project
def add_a_project(title, description, max_grade):
    query = """INSERT INTO Projects VALUES (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s: %s with a maximum grade of %d"%(title, description, max_grade)


# Give a grade to a student
def give_student_grade(github, project, grade):
    query = """INSERT INTO Grades VALUES (?, ?, ?)"""
    DB.execute(query, (github, project, grade))
    CONN.commit()
    print "Successfully added grade %d for %s to %s."%(grade, project, github)

### ** END DB WRITES ** ### 



### ** DB READS ** ### 

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

# Query for projects by title
def project_by_title():
    query = """ """
    DB.execute(query, (args))
    print """\
    """
# Query for a student's grade given a project
def student_grade_by_project():
    query = """ """
    DB.execute(query, (args))
    print """\
    """

# Show all the grades for a student
def show_all_student_grades():
    query = """ """
    DB.execute(query, (args))
    print """\
    """

### ** END DB READS ** ### 

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

        # TODO around here somewhere: If db read, echo user input back,
        # ask if it looks good then commit if they say yes. Move commits out of
        # functions.

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

    CONN.close()

if __name__ == "__main__":
    main()
