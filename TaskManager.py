from Task import Task
import sys
import sqlite3


class TaskManager():
    def __init__(self):
        self.tasks = []

        self.db_server = sqlite3.connect('tdd.db')
        self.db_cursor = self.db_server.cursor()

        self.import_from_db()

    def import_from_db(self):
        # checking if table exists
        self.db_cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tasks'")
        if self.db_cursor.fetchone()[0] == 1:
            # importing data
            self.db_cursor.execute('SELECT * FROM tasks')
            data = self.db_cursor.fetchall()
            for line in data:
                self.new_task(line[0], line[1])
        # table doesn't exist
        else:
            self.db_cursor.execute('''CREATE TABLE tasks(name text, status text)''')

    def loop(self):
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
                    self.db_cursor.execute("DELETE FROM tasks WHERE name='" + self.tasks[tasknumber].name + "'")
                    self.db_server.commit()
                    del self.tasks[tasknumber]
                else:
                    self.db_cursor.execute("UPDATE tasks SET status ='" + value[0] + "' WHERE name='" + self.tasks[tasknumber].name + "'")
                    self.db_server.commit()
                    self.tasks[tasknumber].status = value[0]
        elif value == "q":
            self.db_cursor.close()
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

    def new_task(self, name, status=' '):
        for task in self.tasks:
            if task.name == name:
                return
        self.tasks.append(Task(name, status))
        self.db_cursor.execute("INSERT INTO tasks VALUES ('" + name + "','" + status + "')")
        self.db_server.commit()

    def __str__(self):
        returnvalue = ""
        for taskindex in range(self.tasks.__len__()):
            returnvalue += str(taskindex) + " " + self.tasks[taskindex].__str__()
        return returnvalue
