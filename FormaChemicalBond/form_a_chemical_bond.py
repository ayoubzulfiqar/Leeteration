import collections

def can_form_bond(atoms_string: str, molecule_string: str) -> bool:
    atoms_counts = collections.Counter(atoms_string)
    molecule_counts = collections.Counter(molecule_string)

    for char, count in molecule_counts.items():
        if atoms_counts[char] < count:
            return False
    return True