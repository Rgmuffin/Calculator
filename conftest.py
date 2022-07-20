import pytest
from calculator import Calculator


@pytest.fixture
def supply_calc():
    return Calculator()
