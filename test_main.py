from main import analyze_test


def test_pass_result():
    assert analyze_test("PASS") == "Test passed"


def test_fail_result():
    assert analyze_test("FAIL") == "Test failed"