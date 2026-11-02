from reservation import reserve


def check(label, actual, expected):
    assert actual == expected, f"{label}: actual={actual!r}, expected={expected!r}"
    print(f"PASS {label}: {actual!r}")


def run_checks():
    expected_exact = None  # COMPLETE from requirements
    expected_zero = None  # COMPLETE for reserve(0, 0)
    check("exact capacity", reserve(5, 5), expected_exact)
    check("zero capacity zero request", reserve(0, 0), expected_zero)
    check("below capacity", reserve(5, 2), (True, 3))
    check("above capacity", reserve(5, 6), (False, 5))
    check("zero request positive capacity", reserve(5, 0), (True, 5))
    check("zero capacity positive request", reserve(0, 1), (False, 0))
    capacity = 5
    accepted, remaining = reserve(capacity, 6)
    check("rejection flag", accepted, False)
    check("rejection preserves remaining capacity", remaining, capacity)
    check("caller capacity unchanged", capacity, 5)
    print("Complete regression passed")


if __name__ == "__main__":
    run_checks()
