from reservation import reserve

assert reserve(5, 2) == (True, 3)
assert reserve(5, 6) == (False, 5)
print("Existing checks passed: below and above capacity")
