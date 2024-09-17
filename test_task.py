import task
import pytest
from unittest.mock import patch

@patch('builtins.input', return_value = "Greg")
def test_task_1(mock_input):
    result = task.task_1()
    assert result == ["Greg", "Geoff", "Jeffrey"]

def test_task_2():
    result = task.task_2()
    assert result == {
        "name": "Geoff",
        "age": 35,
        "profession": "technician",
        "car": {
            "make": "Ford",
            "model": "Focus",
            "engine": 1.6,
            "colour": "blue"
        }
    }

def test_task_3(monkeypatch):
    test_data = ("Fred", "Computer Science", 75)
    inputs = iter(test_data)

    monkeypatch.setattr('builtins.input', lambda *args: next(inputs))

    result = task.task_3()
    assert result == ("Geoff", "Maths", 80, "Fred", "Computer Science", 75)

def test_task_4():

    set_1 = {"banana", "cherry", "grape", "mango", "papaya", "lemon"}
    set_2 = {"apple", "pineapple", "orange", "strawberry", "raspberry", "blueberry", "melon"}

    result = task.task_4()
    assert result == [set_1, set_2]