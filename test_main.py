from TaskManager import TaskManager
from Task import Task

def test_check_input():
    tm = TaskManager()

    valid_strings = ["+ New", "x 1", "o 4", "- 1", "q"]
    invalid_strings = ["", " ", "a", "q ", "+New", "-New", "+ ", "x New", "o New"]

    for valid in valid_strings:
        assert tm.check_input(valid)

    for invalid in invalid_strings:
        assert not tm.check_input(invalid)

def test_new_task():
    tm = TaskManager()
    tm.new_task("étendre le linge")
    tm.new_task("faire la vaisselle")

    assert tm.tasks[0].name == "étendre le linge"
    assert tm.tasks[0].status == " "

    assert tm.tasks[1].name == "faire la vaisselle"
    assert tm.tasks[1].status == " "

def test_action():
    tm = TaskManager()

    tm.action("+ newtask")
    tm.action("+ task2")

    assert tm.tasks.__len__() == 2

    tm.action("o 0")
    tm.action("x 1")

    assert tm.tasks[0].status == "o"
    assert tm.tasks[1].status == "x"

    tm.action("- 0")

    assert tm.tasks.__len__() == 1
    assert tm.tasks[0].name == "task2"


test_check_input()
test_new_task()
test_action()
