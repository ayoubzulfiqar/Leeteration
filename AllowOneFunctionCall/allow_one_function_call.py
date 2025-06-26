def once(fn):
    has_been_called = False
    first_call_result = None

    def wrapper(*args, **kwargs):
        nonlocal has_been_called, first_call_result
        if not has_been_called:
            first_call_result = fn(*args, **kwargs)
            has_been_called = True
            return first_call_result
        else:
            return None

    return wrapper