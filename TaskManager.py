from Task import Task
import sys

class TaskManager():
    def __init__(self):
        self.tasks = []

    def user_input(self):
        while True:
            print(self)
            value = input()
            while not self.check_input(value):
                value = input()
            self.action(value)


    def action(self, value):
        if value[0] == "+":
            self.new_task(value[2:])
        elif value[0] in ["-", "x", "o"]:
            tasknumber = int(value[2:])
            if 0 <= tasknumber < self.tasks.__len__():
                if value[0] == "-":
                    del self.tasks[tasknumber]
                else:
                    self.tasks[tasknumber].status = value[0]
        elif value == "q":
            sys.exit()

    def check_input(self, value):
        if value:
            if value[0] in ["+", "-", "x", "o", "q"]:
                if value == "q" and value.__len__() == 1:
                    # user is leaving
                    return True
                elif value.__len__() > 2:
                    if value[1] == " ":
                        if value[0] == "+":
                            # user is entering new task
                            return True
                        elif value[0] in ["x", "o", "-"] and value[2:].isnumeric():
                            # user is updating or deleting a task
                            return True
        # user input is invalid
        return False

    def new_task(self, name):
        self.tasks.append(Task(name))

    def __str__(self):
        returnvalue = ""
        for taskindex in range(self.tasks.__len__()):
            returnvalue += str(taskindex) + " " + self.tasks[taskindex].__str__()
        return returnvalue

