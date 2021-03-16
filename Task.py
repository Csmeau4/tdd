class Task():
    def __init__(self, name):
        self.name = name
        self.status = " "

    def __str__(self):
        return "[" + self.status + "] " + self.name + "\n"
