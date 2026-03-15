import pytest
from src.utils.logger import get_logger
from src.utils.excel_reader import get_test_data
logger = get_logger(__name__)
test_data = get_test_data("testdata/add_data.xlsx", "Sheet1")
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,expected", test_data)
def test_add(calc,a,b,expected):
    logger.info(f"Testing add with {a} and {b}")
    result = calc.add(a, b)
    logger.info(f"Result obtained: {result}")
    assert result == expected

@pytest.mark.regression
def test_add_multiple(calc):
    assert calc.add(10, 20) == 30

def test_sub(calc):
    assert calc.sub(10, 20) == -10