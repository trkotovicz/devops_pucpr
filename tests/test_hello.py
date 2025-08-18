import pytest
from hello import calculator

def test_add(monkeypatch, capsys):
    inputs = iter(['1', '2', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out

def test_subtract(monkeypatch, capsys):
    inputs = iter(['2', '5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "5.0 - 3.0 = 2.0" in captured.out

def test_multiply(monkeypatch, capsys):
    inputs = iter(['3', '2', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "2.0 * 4.0 = 8.0" in captured.out

def test_divide(monkeypatch, capsys):
    inputs = iter(['4', '8', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "8.0 / 2.0 = 4.0" in captured.out

def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(['4', '8', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Error: Division by zero" in captured.out

def test_invalid_choice(monkeypatch, capsys):
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out

def test_invalid_number(monkeypatch, capsys):
    inputs = iter(['1', 'a', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid number" in captured.out