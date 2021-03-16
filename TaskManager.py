from Task import Task

class TaskManager():
    def __init__(self):
        self.tasks = []

    def user_input(self):
        while True:
            value = input()
            if self.check_input(value):
                return value

    def check_input(self, value):
        if value:
            if value[0] in ["+", "-", "x", "o", "q"]:
                if value == "q" and value.__len__() == 1:
                    return True
                elif value[1] == " ":
                    if value[0] in ["+", "-"] and value.__len__() > 2:
                        return True
                    elif value[0] in ["x", "o"]:
                        if value[2:].isnumeric():
                            return True
        return False

    def new_task(self, name):
        self.tasks.append(Task(name, self.tasks.__len__()))

    def __str__(self):
        returnvalue = ""
        for task in self.tasks:
            returnvalue += task.__str__()
        return returnvalue

