def invert_object(obj):
    if isinstance(obj, (int, float)):
        if obj == 0:
            raise ValueError("Cannot invert zero.")
        return 1 / obj
    elif isinstance(obj, bool):
        return not obj
    elif isinstance(obj, (list, str, tuple)):
        return obj[::-1]
    else:
        raise TypeError(f"Inversion not supported for object of type {type(obj).__name__}.")