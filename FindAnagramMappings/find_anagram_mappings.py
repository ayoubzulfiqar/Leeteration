def find_anagram_mappings(A: list[int], B: list[int]) -> list[int]:
    b_map = {}
    for i, num in enumerate(B):
        if num not in b_map:
            b_map[num] = []
        b_map[num].append(i)
    
    P = []
    for num_a in A:
        P.append(b_map[num_a].pop(0))
        
    return P