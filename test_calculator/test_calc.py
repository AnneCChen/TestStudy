import pytest
from pythoncode.Calculator import Calculator


class TestCalculator:
    def setup(self):
        print("set up")

    def teardown(self):
        print("teardown")

    def teardown_class(self):
        print("test ends")

    @pytest.mark.p0
    @pytest.mark.parametrize('a, b, expect', [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def test_add0(self, a, b, expect):
        calc = Calculator()
        result = calc.add(a, b)
        print(result)
        assert result == expect
        #assert result(calc.add())


