# three non functional requirements are operability, reliability, and effectivenes


# Create: make the parameters for each assignment, make the add method, figure out how I want to store them

# an assignemnt will have the parameters, name, course, description, priorty, and duedate
class Assignment:
    def __init__ (self, name, course, description, priority, dueDate):
        self.name =  name
        self.course = course
        self.description = description
        self.priority = priority
        self.dueDate = dueDate

        # assignments will be stored in a list
    AssignmentList = list()
    DeletedAssignments = list()

    # add method
    def add(self):
        self.AssignmentList.append(self)
        print(self.AssignmentList)


    #Read: write how each assignment will be displayed and what part of the assignment will be displayed

    def read(self, name):
        for i in self.AssignmentList:
            if i.name == name:
                print(i)
                return i

    #Delete: write the method to delete an assignment, removing it from the printed list, but adding it to another list incase the user wants
    # re add it later
    def delete(self, name):

        for i in self.AssignmentList:
            if i.name == name:

                # adds assignment to DeletedAssignments list
                self.DeletedAssignments.append(i)
                print(self.DeletedAssignments)
                
                #removes assignment from current assignment list
                self.AssignmentList.remove(i)
                print(self.AssignmentList)
