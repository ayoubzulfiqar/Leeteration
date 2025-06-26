def create_object_from_arrays(keys_array, values_array):
    return dict(zip(keys_array, values_array))

if __name__ == "__main__":
    keys1 = ['name', 'age', 'city']
    values1 = ['Alice', 30, 'New York']
    obj1 = create_object_from_arrays(keys1, values1)
    print(obj1)

    keys2 = ['a', 'b']
    values2 = [1, 2, 3]
    obj2 = create_object_from_arrays(keys2, values2)
    print(obj2)

    keys3 = ['x', 'y', 'z']
    values3 = [10, 20]
    obj3 = create_object_from_arrays(keys3, values3)
    print(obj3)

    keys4 = ['item', 'price', 'item']
    values4 = ['apple', 1.50, 'banana']
    obj4 = create_object_from_arrays(keys4, values4)
    print(obj4)

    keys5 = []
    values5 = []
    obj5 = create_object_from_arrays(keys5, values5)
    print(obj5)