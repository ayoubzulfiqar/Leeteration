def findClosestPerson(x: int, y: int, z: int) -> int:
    """
    Determines which person (1 or 2) reaches Person 3 first.

    Args:
        x: Position of Person 1.
        y: Position of Person 2.
        z: Position of Person 3.

    Returns:
        1 if Person 1 arrives first.
        2 if Person 2 arrives first.
        0 if both arrive at the same time.
    """
    dist_p1_to_p3 = abs(x - z)
    dist_p2_to_p3 = abs(y - z)

    if dist_p1_to_p3 < dist_p2_to_p3:
        return 1
    elif dist_p2_to_p3 < dist_p1_to_p3:
        return 2
    else:
        return 0