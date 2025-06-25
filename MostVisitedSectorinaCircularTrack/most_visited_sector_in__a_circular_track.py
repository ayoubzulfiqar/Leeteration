class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        start_sector = rounds[0]
        end_sector = rounds[-1]
        
        most_visited_sectors = []
        
        if start_sector <= end_sector:
            # The marathon path goes directly from start_sector to end_sector
            # (e.g., if n=4, rounds=[1,3,1,2], the overall path is from 1 to 2,
            # which includes sectors 1 and 2)
            for i in range(start_sector, end_sector + 1):
                most_visited_sectors.append(i)
        else:
            # The marathon path wraps around the track
            # (e.g., if n=4, rounds=[3,1], the overall path is from 3 to 1,
            # which includes sectors 3, 4, and 1)
            
            # First, include sectors from 1 up to end_sector
            for i in range(1, end_sector + 1):
                most_visited_sectors.append(i)
            # Then, include sectors from start_sector up to n
            for i in range(start_sector, n + 1):
                most_visited_sectors.append(i)
                
        # The list 'most_visited_sectors' is constructed in ascending order
        # due to the nature of range() and the order of appending.
        return most_visited_sectors