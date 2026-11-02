from reservation import reserve

for capacity, requested in [(5, 2), (5, 5), (5, 6)]:
    print(f"capacity={capacity}, requested={requested}: {reserve(capacity, requested)}")
