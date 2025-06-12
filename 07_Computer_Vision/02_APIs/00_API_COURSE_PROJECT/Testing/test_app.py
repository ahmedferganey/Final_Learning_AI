import pytest

# --------------------------------
# ✅ Functions to be tested
# --------------------------------
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def write_message(filepath, message):
    with open(filepath, 'w') as f:
        f.write(message)

# --------------------------------
# ✅ Basic tests
# --------------------------------
def test_add():
    assert add(1, 1) == 2

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)

# --------------------------------
# ✅ Parametrized tests
# --------------------------------
@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_param(num1, num2, expected):
    assert add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (100, -50, 50),
], ids=["pos+pos", "neg+neg", "pos+neg"])
def test_add_custom_names(num1, num2, expected):
    assert add(num1, num2) == expected

# --------------------------------
# ✅ Fixtures
# --------------------------------
@pytest.fixture
def sample_data():
    return {"a": 10, "b": 5}

def test_subtract_with_fixture(sample_data):
    assert subtract(sample_data["a"], sample_data["b"]) == 5

# Autouse fixture for setup/teardown logging
@pytest.fixture(autouse=True)
def auto_print():
    print("\n[Setup] Starting test")
    yield
    print("[Teardown] Ending test")

# --------------------------------
# ✅ Temp file test
# --------------------------------
def test_write_message(tmp_path):
    file_path = tmp_path / "message.txt"
    write_message(file_path, "Hello, pytest!")
    assert file_path.read_text() == "Hello, pytest!"

# --------------------------------
# ✅ Indirect parametrization
# --------------------------------
@pytest.fixture
def number(request):
    return request.param

@pytest.mark.parametrize("number", [5, 10, 15], indirect=True)
def test_multiply_by_two(number):
    assert multiply(number, 2) == number * 2

# --------------------------------
# ✅ Skips and expected failures
# --------------------------------
@pytest.mark.skip(reason="Example of a skipped test")
def test_skipped():
    assert add(2, 2) == 5  # Incorrect on purpose

@pytest.mark.skipif(True, reason="Conditionally skipped for demo")
def test_conditional_skip():
    assert subtract(5, 5) == 0

@pytest.mark.xfail(reason="Expected to fail demonstration")
def test_expected_fail():
    assert add(2, 2) == 5  # Incorrect on purpose

# --------------------------------
# ✅ Optional: Class-based grouping
# --------------------------------
class TestMathOperations:
    def test_add(self):
        assert add(3, 4) == 7

    def test_subtract(self):
        assert subtract(10, 5) == 5

# --------------------------------
# ✅ Benchmarking (optional, install pytest-benchmark)
# --------------------------------
def test_add_benchmark(benchmark):
    result = benchmark(add, 100, 200)
    assert result == 300
