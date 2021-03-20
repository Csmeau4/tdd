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
    initial_length = tm.tasks.__len__()
    tm.new_task("étendre le linge")
    tm.new_task("faire la vaisselle")
    new_length = tm.tasks.__len__()

    assert tm.tasks[new_length - 2].name == "étendre le linge"
    assert tm.tasks[new_length - 2].status == " "

    assert tm.tasks[new_length - 1].name == "faire la vaisselle"
    assert tm.tasks[new_length - 1].status == " "

    task_amount = tm.tasks.__len__()
    tm.new_task("étendre le linge")
    assert task_amount == tm.tasks.__len__()

    # Removing changes

    tm.action("- " + str(new_length - 1))
    tm.action("- " + str(new_length - 2))

    assert tm.tasks.__len__() == initial_length


def test_action():
    tm = TaskManager()
    initial_length = tm.tasks.__len__()

    tm.action("+ newtask")
    tm.action("+ task2")

    new_length = tm.tasks.__len__()

    assert new_length == initial_length + 2

    tm.action("o " + str(new_length - 2))
    tm.action("x " + str(new_length - 1))

    assert tm.tasks[-2].status == "o"
    assert tm.tasks[-1].status == "x"

    # Removing changes

    tm.action("- " + str(new_length - 1))
    tm.action("- " + str(new_length - 2))

    assert tm.tasks.__len__() == initial_length


test_check_input()
test_new_task()
test_action()
