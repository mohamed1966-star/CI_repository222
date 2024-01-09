import calculator

class TestCalc:
    def test_sum(self):
        assert 555 == calculator.sum(4, 4)