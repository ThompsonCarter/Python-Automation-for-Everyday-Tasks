# Install pytest: pip install pytest
from utils import calc_discount

def test_calc_discount():
    assert calc_discount(100, 0.1) == 90
# Run: pytest -q
