def analyze_test(result):
    if result == "PASS":
        return "Test passed"
    else:
        return "Test failed"


print(analyze_test("PASS"))