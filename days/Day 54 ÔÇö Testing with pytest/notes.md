# Day 54 — Testing with pytest

## Key syntax
```python
# Basic test
def test_something():
    assert result == expected

# Raises
with pytest.raises(ValueError):
    bad_function()

# Fixture
@pytest.fixture
def client():
    return MyClient()

def test_with_fixture(client):
    assert client.ping() == 'pong'

# Parametrize
@pytest.mark.parametrize('n,expected', [(1,1),(2,4),(3,9)])
def test_square(n, expected):
    assert n**2 == expected

# Mock
from unittest.mock import patch, MagicMock
@patch('module.function')
def test_mocked(mock_fn):
    mock_fn.return_value = 42
    assert some_fn() == 42
    mock_fn.assert_called_once()
```

## What to test
- Happy path (normal inputs)
- Edge cases (empty, None, zero, single)
- Error cases (invalid input, raises)
- Boundary conditions (min/max values)

## Interview tips
- Tests = documentation that never goes out of date
- Aim for isolated unit tests — mock external dependencies
- Good test name: `test_<what>_<when>_<expected>`
