import pytest
from how_many_bobs_main import bob_count_func

class TestTakesReturns:
    @pytest.mark.it("Function takes string and returns integer.")
    def test_func_takes_string_and_returns_int(self):
        test_string = "test"
        assert isinstance(bob_count_func(test_string), int)

class TestFunctionCountsBobsBasics:
    @pytest.mark.it("Function counts no bobs in empty strings.")
    def test_funct_no_bobs(self):
        test_string = ""
        assert bob_count_func(test_string) == 0
    @pytest.mark.it("Function counts 1 bob in string \"bob\".")
    def test_1_bob(self):
        test_string = "bob"
        assert bob_count_func(test_string) == 1

class TestCountsBobsSpec:
    @pytest.mark.it("Function counts bobs correctly from strings.")
    def test_func_counts_bobs(self):
        test_string_1 = "babbobbobabrbb"
        test_string_2 = "boobobbobobdasdabbo"
        test_string_3 = "ogbobbobobozobobojbobobsobob"
        assert bob_count_func(test_string_1) == 2
        assert bob_count_func(test_string_2) == 3
        assert bob_count_func(test_string_3) == 7