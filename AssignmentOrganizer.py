# takes user input to create the list of assignments and use Assignment functions

from AssignmentObj import Assignment


if __name__ == "__main__":
    while True:
        service = input("what would you like to do?")

        if service == "add":
            #request for adding assignment
            # name, course, description, priority, dueDate
            name = input("what is the name of the assignment?")
            course = input("what is the course for the assignment")
            description = input("what is the description of the assignment?")
            priority = input("what is the priority of the assignment from 1-5, 1 being low?")
            dueDate = input("what is the due date of the assignment, in a 00/00/0000 format")
            
            newAssignment = Assignment(name, course, description, priority, dueDate)
            newAssignment.add()
        
        if service == "read":
            name = input("what is the name of the assingment you want to read?")
            newAssignment.read(name)
        
        if service == "delete":
            name = input("what is the name of the assignment you want to delete?")
            newAssignment.delete(name)

        

        
