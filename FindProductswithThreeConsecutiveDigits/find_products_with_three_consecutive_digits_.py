def has_three_consecutive_digits(n):
    s_n = str(n)
    if len(s_n) < 3:
        return False
    for i in range(len(s_n) - 2):
        d1 = int(s_n[i])
        d2 = int(s_n[i+1])
        d3 = int(s_n[i+2])
        if d2 == d1 + 1 and d3 == d2 + 1:
            return True
    return False

def find_products_with_three_consecutive_digits(max_factor=100):
    found_products = set()
    for i in range(1, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if has_three_consecutive_digits(product):
                found_products.add(product)
    return sorted(list(found_products))

if __name__ == "__main__":
    products = find_products_with_three_consecutive_digits(max_factor=100)
    for p in products:
        print(p)