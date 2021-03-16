from Task import Task

class TaskManager():
    def __init__(self):
        self.tasks = []

    def user_input(self):
        while True:
            value = input()
            while not self.check_input(value):
                value = input()




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
                        elif value[0] in ["x", "o", "-"]:
                            if value[2:].isnumeric():
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

