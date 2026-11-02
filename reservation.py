def reserve(capacity, requested):
    if requested < capacity:
        return True, capacity - requested
    return False, capacity
