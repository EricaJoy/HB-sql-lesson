import sqlite3

DB = None
CONN = None


### DB QUERY FUNCTIONS ###

### ** DB READS ** ### 
# These can probably be dictionaries. Investigate later.

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github 
               FROM Students
               WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

# Query for projects by title (handles multi-result responses...maybe)
def project_by_title(title):
    query = """SELECT DISTINCT title, description 
               FROM Projects 
               WHERE title = ? 
               ORDER BY title"""
    result = DB.execute(query, (title,))
    print "Here are projects containing %s: \n"%(title)
    for i in result.fetchall(): 
        print """
        Project Name: %s
        Project Description: %s
        \n
        """%(i[0], i[1])

# Query for a student's grade given a project
def student_grade_by_project(first_name, last_name, project):
    query = """SELECT ?, grade 
               FROM Grades JOIN Students 
               WHERE (Students.github = Grades.student_github)
               AND Student.first_name = ?
               AND Student.last_name = ?"""
    result = DB.execute(query, (project, first_name, last_name))
    print "Here are %s %s's grades for %s"%(first_name, last_name, project)
    for i in result.fetchall():
        print """\
        Project Name: %s
        Grade: %d
        \n
        """%(i[0], i[1])

# Show all the grades for a student
# TODO handle query by github case
def show_all_student_grades(first_name, last_name):
    query = """SELECT grade 
               FROM Grades JOIN Students
               WHERE (Students.github = Grades.student_github)
               AND Students.first_name=?
               AND Students.last_name= ?"""
    result = DB.execute(query, (first_name, last_name))
    print "%s %s's grades are:\n"%(first_name, last_name)
    for i in result.fetchall():
        print " %d "%i[0]

### ** END DB READS ** ### 

### ** DB WRITES ** ### 

# Add a student
def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github)) # Is there any situation where DB.execute doesn't take a tuple?
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

# Add a project
def add_a_project(title, description, max_grade):    
    max_grade = int(max_grade)
    query = """INSERT INTO Projects (title, description, max_grade) VALUES (?, ?, ?)"""
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
        # functions...or not because this is just stuff for the next project.

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            project_by_title(*args)
        elif command == "student_grade_project":
            student_grade_by_project(*args)
        elif command == "student_grades":
            show_all_student_grades(*args)
        elif command == "add_project":    
            title = args[0]
            description = " ".join([i for i in args[1:-1]])
            grade = args[-1]
            add_a_project(title, description, grade)
        elif command == "give_grade":    
            give_student_grade(*args)


    CONN.close()

if __name__ == "__main__":
    main()
