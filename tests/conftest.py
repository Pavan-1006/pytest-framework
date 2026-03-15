import pytest
from src.utils.logger import get_logger

logger = get_logger("failure_logger")
from src.calculator import Calculator
@pytest.fixture
def calc():
    return Calculator()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger.error(f"Test Failed: {item.name}")
        logger.error(f"Location: {item.nodeid}")
        logger.error(f"Error: {report.longrepr}")