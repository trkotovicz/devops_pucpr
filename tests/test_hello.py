"""Tests for the simple calculator."""
from hello import calculator


def test_add(monkeypatch, capsys):
    """Testa a soma."""
    inputs = iter(['1', '2', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out


def test_subtract(monkeypatch, capsys):
    """Testa a subtração."""
    inputs = iter(['2', '5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "5.0 - 3.0 = 2.0" in captured.out


def test_multiply(monkeypatch, capsys):
    """Testa a multiplicação."""
    inputs = iter(['3', '2', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "2.0 * 4.0 = 8.0" in captured.out


def test_divide(monkeypatch, capsys):
    """Testa a divisão."""
    inputs = iter(['4', '8', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "8.0 / 2.0 = 4.0" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    """Testa a divisão por zero."""
    inputs = iter(['4', '8', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Error: Division by zero" in captured.out


def test_invalid_choice(monkeypatch, capsys):
    """Testa escolha inválida."""
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out


def test_invalid_number(monkeypatch, capsys):
    """Testa número inválido."""
    inputs = iter(['1', 'a', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator()
    captured = capsys.readouterr()
    assert "Invalid number" in captured.out
