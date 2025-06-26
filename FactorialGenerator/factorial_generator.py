def factorial_generator(n_terms):
    if n_terms <= 0:
        return

    current_factorial = 1
    yield current_factorial

    for i in range(1, n_terms):
        current_factorial *= i
        yield current_factorial

if __name__ == "__main__":
    for fact in factorial_generator(10):
        print(fact)

    for fact in factorial_generator(5):
        print(fact)

    for fact in factorial_generator(1):
        print(fact)

    for fact in factorial_generator(0):
        print(fact)