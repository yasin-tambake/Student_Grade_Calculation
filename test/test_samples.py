from src.app import calculator, grade

def test_calculator():
    total, percent = calculator(85, 90, 78, 92, 88)
    assert total == 433
    assert percent == 86.6

    total, percent = calculator(50, 60, 70, 80, 90)
    assert total == 350
    assert percent == 70.0

def test_grade():
    assert grade(95) == 'A+'
    assert grade(85) == 'A'
    assert grade(75) == 'B'
    assert grade(65) == 'C'
    assert grade(55) == 'D'
    assert grade(45) == 'Fail'
    assert grade(0) == 'Fail'