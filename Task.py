class Task():
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.status = " "

    def __str__(self):
        return str(self.number) + " [" + self.status + "] " + self.name + "\n"
